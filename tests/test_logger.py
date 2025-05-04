"""Test level module test_cli for dailylog."""

from pathlib import Path

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem

from dailylog_lib.logger import Logger
from tests.conftest import _occ_file, _occ_str

LOG_FN = "/var/log/daily.log"
CACHE_KEY = "test"
MESSAGE = "Do not eat yellow snow."
MATCH_FMT = "{0}: {1} - Do not eat yellow snow.\n"


def test_cached_logger(fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]):
    """Test use/creation of non default log."""
    # cfg_fn = str(DEFAULTS.get("config", ""))
    # cache_fn = str(DEFAULTS.get("cache", ""))
    fs.create_dir(Path(LOG_FN).parent)
    logger = Logger()
    logger.log(MESSAGE, logfn=LOG_FN, label="INFO", key=CACHE_KEY)
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    assert _occ_str(MESSAGE, err) == 1
    assert _occ_file(LOG_FN, MESSAGE) == 1


def test_logger_level_default(fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]):
    """Test only first message to stderr."""
    # cfg_fn = str(DEFAULTS.get("config", ""))
    # cache_fn = str(DEFAULTS.get("cache", ""))
    fs.create_dir(Path(LOG_FN).parent)
    logger = Logger()
    logger.debug(MESSAGE, logfn=LOG_FN, caller="testing")
    logger.warning(MESSAGE, logfn=LOG_FN, caller="testing")
    logger.info(MESSAGE, logfn=LOG_FN, caller="testing")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    assert _occ_str(MESSAGE, err) == 1
    assert _occ_file(LOG_FN, MESSAGE) == 1


def test_logger_level_debug(fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]):
    """Test only first message to stderr."""
    # cfg_fn = str(DEFAULTS.get("config", ""))
    # cache_fn = str(DEFAULTS.get("cache", ""))
    fs.create_dir(Path(LOG_FN).parent)
    logger = Logger(level="DEBUG")
    logger.debug(MESSAGE, logfn=LOG_FN, caller="testing")
    logger.info(MESSAGE, logfn=LOG_FN, caller="testing")
    logger.warning(MESSAGE, logfn=LOG_FN, caller="testing")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    assert _occ_str(MESSAGE, err) == 3
    assert _occ_file(LOG_FN, MESSAGE) == 3


def test_logger_level_info(fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]):
    """Test logging info."""
    # cfg_fn = str(DEFAULTS.get("config", ""))
    # cache_fn = str(DEFAULTS.get("cache", ""))
    fs.create_dir(Path(LOG_FN).parent)
    logger = Logger(level="INFO")
    logger.info(MESSAGE, logfn=LOG_FN, caller="testing")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    match = MATCH_FMT.format("INFO", "testing")
    assert _occ_str(match, err) == 1
    assert _occ_file(LOG_FN, match) == 1


def test_logger_level_warning(fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]):
    """Test logging warning."""
    # cfg_fn = str(DEFAULTS.get("config", ""))
    # cache_fn = str(DEFAULTS.get("cache", ""))
    fs.create_dir(Path(LOG_FN).parent)
    logger = Logger()
    logger.warning(MESSAGE, logfn=LOG_FN, caller="testing")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    match = MATCH_FMT.format("WARNING", "testing")
    assert _occ_str(match, err) == 1
    assert _occ_file(LOG_FN, match) == 1


def test_logger_level_error(fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]):
    """Test logging error."""
    fs.create_dir(Path(LOG_FN).parent)
    logger = Logger()
    logger.error(MESSAGE, logfn=LOG_FN, caller="testing")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    match = MATCH_FMT.format("ERROR", "testing")
    assert _occ_str(match, err) == 1
    assert _occ_file(LOG_FN, match) == 1


def test_logger_level_critical(fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]):
    """Test logging critical."""
    fs.create_dir(Path(LOG_FN).parent)
    logger = Logger()
    logger.critical(MESSAGE, logfn=LOG_FN, caller="testing")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    match = MATCH_FMT.format("CRITICAL", "testing")
    assert _occ_str(match, err) == 1
    assert _occ_file(LOG_FN, match) == 1
