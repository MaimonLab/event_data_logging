# event_data_logging

**POSSIBLE PACKAGE NAMES**

- event_data_logging
- json_csv_saver
- data_saver
- maimon-data-saver

Save events to json or csv files. This package comes in 4 flavors:

- CSVWriter
- StampedCSVWriter
- JSONWriter
- StampedJSONWriter

The StampedWriters will add a leading entry with the current timestamp to your event or line. The default format is in seconds with fraction of a second as decimal numbers. Alternatlively you can save the timestamps as nanoseconds instead.

## Install

To install from our private github repo : 

    pip install git+ssh://git@github.com/MaimonLab/event_data_logging.git


Once openly released, the following should work :

    pip install git+https://git@github.com/maimonlab/event_data_logging.git

Eventually, we might install it on pypi, then we can simply do

    pip install event_data_logging

## Usage

### JSON example without timestamps

```python
from event_data_logging.json_saver import JSONWriter
test_events = [
    {"bar_color": [1, 2, 3]},
    {"bar_width_degrees": 10},
    {"example_float": 0.1},
]
filename = "data/json_data.json"
writer = JSONWriter(filename)
for event in test_events:
    writer.save_event(event)
```

This would create the file `data/json_data.json` with content:

```
[
{"bar_color": [1, 2, 3]},
{"bar_width_degrees": 10},
{"example_float": 0.1}
]
```

### JSON example with timestamp

```python
from event_data_logging.json_saver import StampedJSONWriter
test_events = [
    {"bar_color": [1, 2, 3]},
    {"bar_width_degrees": 10},
    {"example_float": 0.1},
]
filename = "data/stamped_json_data.json"
writer = StampedJSONWriter(filename)
for event in test_events:
    writer.save_event(event)
```

This would create the file `data/stamped_json_data.json` with content:

```
[
{"timestamp": 1661201947.0682852, "bar_color": [1, 2, 3]},
{"timestamp": 1661201947.0683577, "bar_width_degrees": 10},
{"timestamp": 1661201947.0684075, "example_float": 0.1}
]
```

### CSV example with nanosecond timestamp

```python
from event_data_logging.csv_saver import StampedCSVWriter, TimestampModes
filename = "data/csv_data.csv"
xyz_header = ["x", "y", "z"]
csv_writer = StampedCSVWriter(
    filename, header=xyz_header, timestamp_mode=TimestampModes.NANOSECONDS
)
for i in range(3):
    line = [
        str(10 * i + 1),
        str(10 * i + 2),
        str(10 * i + 3),
    ]
    csv_writer.save_line(line)
```

This will give the file `data/csv_data.csv` with the following content:

```
timestamp,x,y,z
1661110000123456789,1,2,3
1661110001123456789,11,12,13
1661110002123456789,21,22,23
```

## Developing

You can run the tests with pytest, and check the coverage. To do so, use the following commands:

    coverage run -m pytest

The coverage report prints to the terminal with:

    coverage report

This report shows how much of all the code is actually run during the test.

# ros2_message_handling using outside dependencies

In our lab, this package is mainly used to save ros2 data, and thus turning ros2 messages to dictionaries is very common. The ros2_message_handling module therefore requires some ros2 packages to be installed, and is outside of the scope of most uses.

_The `test_ros2_message_handling.py` will thus fail in environments without ROS2.
\_We will likely remove this module before the stable release. the ros2_message handling should be integrated in it's own ros packages_
