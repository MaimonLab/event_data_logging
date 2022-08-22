from collections import OrderedDict
from geometry_msgs.msg import TwistStamped

from event_data_logging.ros2_message_handling import (
    convert_ros2_msg_to_nanosecond_stamped_dict,
)


def test_convert_ros2_msg_to_nanosecond_stamped_dict():

    message = TwistStamped()
    # custom_dict = convert_ros2_msg_to_maimon_dict(message)
    custom_dict = convert_ros2_msg_to_nanosecond_stamped_dict(message)
    print(f"Custom dict: {custom_dict}")
    test_dict = OrderedDict(
        [
            ("timestamp", 0.0),
            ("frame_id", ""),
            (
                "twist",
                OrderedDict(
                    [
                        ("linear", OrderedDict([("x", 0.0), ("y", 0.0), ("z", 0.0)])),
                        ("angular", OrderedDict([("x", 0.0), ("y", 0.0), ("z", 0.0)])),
                    ]
                ),
            ),
        ]
    )

    assert custom_dict == test_dict
