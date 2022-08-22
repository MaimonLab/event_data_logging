#!/usr/bin/env python3
import numpy as np
from collections import OrderedDict


def flatten_dictionary(
    partial_dict, header=None, data_row=None, parent_field_name=None, parent_idx=None
):
    """flattens the message by finding all its fields, adding it to the list if float, int, string or array.
    If the field is a sub-message, it will call flatten_recursive on the field.
    the prepend_field builds up the header name, ensuring that the header contains information of prior unpackings.
    """

    if header is None:
        header = []
    if data_row is None:
        data_row = []

    for key, item in partial_dict.items():

        if parent_field_name is not None:
            accumulated_field_name = f"{parent_field_name}_{key}"
        else:
            accumulated_field_name = key

        # if the item is a float, int or string, we can simply append
        if isinstance(item, (int, float, str)):
            if parent_idx is not None:
                header.append(f"{accumulated_field_name}_{parent_idx}")
            else:
                header.append(accumulated_field_name)
            data_row.append(item)

        # if the item is an array, we must unpack it.
        # we'll give it a name of fieldname_0, fieldname_1, ...
        elif type(item) == np.ndarray:
            data_row.extend(item.tolist())
            for i in range(len(item)):
                header.append(f"{accumulated_field_name}_{i}")

        elif type(item) == list:
            if type(item[0]) in [dict, OrderedDict]:
                for i, list_item in enumerate(item):
                    header, data_row = flatten_dictionary(
                        list_item,
                        header,
                        data_row,
                        accumulated_field_name,
                        parent_idx=i,
                    )
            else:
                data_row.extend(item)
                for i in range(len(item)):
                    header.append(f"{accumulated_field_name}_{i}")

        # if the item has fields, we need to flatten it more. We call it with the accumulated field name
        # elif hasattr(sub_item, "get_fields_and_field_types"):
        elif type(item) in [dict, OrderedDict]:

            header, data_row = flatten_dictionary(
                item, header, data_row, accumulated_field_name
            )
        else:
            raise Exception(f"Message format is not implemented")

    return header, data_row
