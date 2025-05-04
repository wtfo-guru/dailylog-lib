"""Tests level module test_log_levels for dailylog-lib."""

import logging

from dailylog_lib.logger import LOG_LEVELS, log_label, log_level


def test_creation_default_config() -> None:
    """Test creation of default config."""
    for key in LOG_LEVELS.keys():
        assert log_level(key) == LOG_LEVELS[key]
        assert log_label(str(LOG_LEVELS[key])) == key
    assert log_level("42") == logging.WARNING
    assert log_label("wtf") == "WARNING"
