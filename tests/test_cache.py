"""Test level module test_cli for dailylog."""

from pathlib import Path

import pytest
from pyfakefs.fake_filesystem import FakeFilesystem
from wtforglib.files import load_json_file, load_yaml_file

from dailylog_lib.cache import CONST_CACHE_VERSION, Cache
from dailylog_lib.config import CURRENT_CONFIG_VERSION  # CONST_DEFAULT_LOG
from dailylog_lib.constants import DEFAULTS
from tests.conftest import _occ_file, _occ_str

CACHE_FN = "/tmp/daily.cache"
CONFIG_FN = "/tmp/daily.config"
LOG_FN = "/var/log/daily.log"
CACHE_KEY = "test"
MESSAGE = "Do not eat yellow snow."
TD = Path(__file__).parent.resolve() / "data"
T_CACHE = TD / "dailylog.json"
LOG_ALT = "/usr/local/var/log/daily.log"
CONFIG_DATA = """default_log: /usr/local/var/log/daily.log
version: 1
"""


def test_creation_default_config(fs: FakeFilesystem) -> None:
    """Test creation of default config."""
    cfg_fn = str(DEFAULTS.get("config", ""))
    cache_fn = str(DEFAULTS.get("cache", ""))
    fs.add_real_file(T_CACHE, target_path=cache_fn)
    fs.create_file(cfg_fn, contents=CONFIG_DATA)
    Cache()
    assert Path(cfg_fn).is_file()
    assert Path(cache_fn).is_file()
    cached_data = load_json_file(cache_fn)
    assert cached_data.get("version", 0) == CONST_CACHE_VERSION
    config_data = load_yaml_file(cfg_fn)
    assert config_data.get("version", 0) == CURRENT_CONFIG_VERSION
    assert config_data.get("default_log", 0) == LOG_ALT


def test_creation_non_default_log(
    fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test use/creation of non default log."""
    # cfg_fn = str(DEFAULTS.get("config", ""))
    # cache_fn = str(DEFAULTS.get("cache", ""))
    fs.create_dir(Path(LOG_FN).parent)
    logger = Cache()
    logger.log_message(CACHE_KEY, MESSAGE, logfn=LOG_FN, label="INFO")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    assert _occ_str(MESSAGE, err) == 1
    assert _occ_file(LOG_FN, MESSAGE) == 1


def test_creation_set_default_log(fs: FakeFilesystem) -> None:  # noqa: WPS218
    """Test setting alternate default log."""
    logger = Cache(cache=CACHE_FN, config=CONFIG_FN)
    with pytest.raises(FileNotFoundError):
        logger.set_default_log(LOG_FN)
    fs.create_dir(Path(LOG_FN).parent)
    logger.set_default_log(LOG_FN)
    logger.log_message(CACHE_KEY, MESSAGE, logfn=LOG_FN, label="ERROR")
    assert Path(CONFIG_FN).is_file()
    assert Path(CACHE_FN).is_file()
    assert Path(LOG_FN).is_file()
    cached_data = load_json_file(CACHE_FN)
    assert cached_data.get("version", 0) == CONST_CACHE_VERSION
    config_data = load_yaml_file(CONFIG_FN)
    assert config_data.get("version", 0) == CURRENT_CONFIG_VERSION
    assert config_data.get("default_log", 0) == LOG_FN


def test_caching(fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]) -> None:
    """Test only first message to stderr."""
    # cfg_fn = str(DEFAULTS.get("config", ""))
    # cache_fn = str(DEFAULTS.get("cache", ""))
    fs.create_dir(Path(LOG_FN).parent)
    logger = Cache()
    logger.log_message(CACHE_KEY, MESSAGE, logfn=LOG_FN, label="DEBUG")
    logger.log_message(CACHE_KEY, MESSAGE, logfn=LOG_FN, label="WARNING")
    logger.log_message(CACHE_KEY, MESSAGE, logfn=LOG_FN, label="INFO")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    assert _occ_str(MESSAGE, err) == 1
    assert _occ_file(LOG_FN, MESSAGE) == 3


def test_caching_quietly(
    fs: FakeFilesystem, capsys: pytest.CaptureFixture[str]
) -> None:
    """Test only first message to stderr."""
    # cfg_fn = str(DEFAULTS.get("config", ""))
    # cache_fn = str(DEFAULTS.get("cache", ""))
    fs.create_dir(Path(LOG_FN).parent)
    logger = Cache()
    logger.log_message(CACHE_KEY, MESSAGE, quiet=True, logfn=LOG_FN, label="DEBUG")
    logger.log_message(CACHE_KEY, MESSAGE, quiet=True, logfn=LOG_FN, label="WARNING")
    logger.log_message(CACHE_KEY, MESSAGE, quiet=True, logfn=LOG_FN, label="INFO")
    assert Path(LOG_FN).is_file()
    out, err = capsys.readouterr()
    assert _occ_str(MESSAGE, err) == 0
    assert _occ_file(LOG_FN, MESSAGE) == 3
