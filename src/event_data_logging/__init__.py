"""
The imports make it possible to import:
  from src.event_data_logging import JSONWriter
instead of:
  from src.event_data_logging.json_writer import JSONWriter
"""

__version__ = "0.1.2"


from src.event_data_logging.json_writer import JSONWriter, StampedJSONWriter, TimestampModes
from src.event_data_logging.csv_writer import CSVWriter, StampedCSVWriter
