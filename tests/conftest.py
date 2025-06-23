"""Test level module test_cli for dailylog."""


def _occ_str(needle: str, haystack: str) -> int:
    """Count the number of times needle occurs in haystack."""
    return haystack.count(needle)


def _occ_file(fn: str, needle: str) -> int:
    """Count the number of times needle occurs in file."""
    with open(fn, "r") as fd:
        return _occ_str(needle, fd.read())
