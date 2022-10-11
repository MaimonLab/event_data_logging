import pytest
from pathlib import Path


def pytest_addoption(parser):
    parser.addoption(
        "--ros-dependent",
        action="store_true",
        dest="ros_dependent",
        default=False,
        help="Run tests that depend on ros environment",
    )
