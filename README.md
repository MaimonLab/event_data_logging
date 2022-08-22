# maimon-save-events

Save events to json or csv files. This package comes in 4 flavors:

- CSVWriter
- StampedCSVWriter
- JSONWriter
- StampedJSONWriter

## Basic usage

```
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

This would result in a file containing the following:

```
[
{"timestamp": 1661110000123456789, "bar_color": [1, 2, 3]},
{"timestamp": 1661110010123456789, "bar_width_degrees": 10},
{"timestamp": 1661110020123456789, "example_float": 0.1}
]
```

## Developing

    You can run the tests with pytest, and check the coverage. To do so, use the following commands:

        coverage run -m pytest

    The coverage report prints to the terminal with:

        coverage report

    This report shows how much of all the code is actually run during the test.
