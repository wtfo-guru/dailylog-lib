"""Test level module test_foos for dailylog-lib."""

from dailylog_lib.foos import banner

ONE = "----- Test Banner -----"
TWO = "===== Test Banner started ====="
THREE = "----- Test Banner exiting -----"


def test_banner() -> None:
    """Test use/creation of non default log."""
    res = banner("Test Banner", width=10)
    assert res == ONE


def test_banner_two() -> None:
    """Test use/creation of non default log."""
    res = banner("Test Banner", width=10, action=True, char="=")
    assert res == TWO


def test_banner_three() -> None:
    """Test use/creation of non default log."""
    res = banner("Test Banner", width=10, action=False)
    assert res == THREE
