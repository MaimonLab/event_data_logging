#!/usr/bin/env python3

import csv
from dataclasses import dataclass
import time
from event_data_logging.file_handling import validate_filename


class CSVWriter:
    def __init__(self, goal_filename, header=None):

        self.filename = validate_filename(goal_filename)

        self.header_initialized = False
        if header is not None:
            self.save_header(header)
            self.header_initialized = True

    def save_line(self, line_to_save):
        with open(self.filename, "a+") as file:
            writer = csv.writer(file)
            writer.writerow(line_to_save)

    def save_header(self, header_line):
        with open(self.filename, "w") as file:
            writer = csv.writer(file)
            writer.writerow(header_line)


@dataclass
class TimestampModes:
    SECONDS: int = 1
    NANOSECONDS: int = 2


class StampedCSVWriter(CSVWriter):
    def __init__(self, filename, header=None, timestamp_mode=TimestampModes.SECONDS):

        if header is not None:
            header = ["timestamp", *header]

        CSVWriter.__init__(self, filename, header)
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

        self._timestamp_mode = timestamp_mode

    def save_line(self, data):

        if self._timestamp_mode == TimestampModes.SECONDS:
            timestamp = time.time()
        elif self._timestamp_mode == TimestampModes.NANOSECONDS:
            timestamp = time.time_ns()

        stamped_data = [timestamp, *data]

        super().save_line(stamped_data)
