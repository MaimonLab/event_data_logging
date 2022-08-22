from rosidl_runtime_py.convert import message_to_ordereddict
from collections import OrderedDict


def convert_ros2_msg_to_nanosecond_stamped_dict(message):
    # convert message in our format of dictionary
    ordered_dict = message_to_ordereddict(message)
    timestamp = (
        ordered_dict["header"]["stamp"]["sec"] * 1e9
        + ordered_dict["header"]["stamp"]["nanosec"]
    )
    custom_dict = OrderedDict(
        [("timestamp", timestamp), ("frame_id", ordered_dict["header"]["frame_id"])]
    )
    del ordered_dict["header"]
    custom_dict.update(ordered_dict)
    return custom_dict
