import json
import time
import os
from typing import Dict
from dataclasses import dataclass

from event_data_logging.file_handling import validate_filename


class JSONWriter:
    def __init__(self, goal_filename) -> None:

        self.filename = validate_filename(goal_filename)
        self.header_initialized = False

    def save_event(self, save_data: Dict):
        """Saves a dict of event data along with the current timestamp.

        Args:
            data (dict): Dictionary of event data to save,
            eg {param_name : param_value} for a parameter change
        """

        data_string = json.dumps(save_data, ensure_ascii=False)

        if not self.header_initialized:
            with open(self.filename, "wb") as f:
                f.write("[\n".encode("utf8"))
                f.write(data_string.encode("utf8"))
                f.write("\n]".encode("utf8"))
                self.header_initialized = True

        else:
            with open(self.filename, "r+b") as f:
                f.seek(-1, os.SEEK_END)
                cur_char = f.read(1)
                # seek to before previous "\n]" end of file.
                while cur_char in [b"\n", b"]"]:
                    f.seek(-2, os.SEEK_CUR)
                    cur_char = f.read(1)
                # and delete remainder.
                f.truncate()
                # write new data.
                f.write(",\n".encode("utf8"))
                f.write(data_string.encode("utf8"))
                f.write("\n]".encode("utf8"))


@dataclass
class TimestampModes:
    SECONDS: int = 1
    NANOSECONDS: int = 2


class StampedJSONWriter(JSONWriter):
    def __init__(self, filename, timestamp_mode=TimestampModes.SECONDS):
        JSONWriter.__init__(self, filename)
        self._timestamp_mode = timestamp_mode

    @property
    def timestamp_mode(self):
        return self._timestamp_mode

    @timestamp_mode.setter
    def timestamp_mode(self, timestamp_mode):

        if type(timestamp_mode) != int:
            raise TypeError("timestamp mode must be int")

        if timestamp_mode not in [1, 2]:
            raise Exception(f"Invalid timestamp integer")

        # if timestamp_mode == TimestampModes.SECOND:
        self._timestamp_mode = timestamp_mode

    def save_event(self, data):

        if self._timestamp_mode == TimestampModes.SECONDS:
            timestamp = time.time()
        elif self._timestamp_mode == TimestampModes.NANOSECONDS:
            timestamp = time.time_ns()

        stamped_data = {"timestamp": timestamp, **data}

        super().save_event(stamped_data)
