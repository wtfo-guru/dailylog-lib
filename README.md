# dailylog

[![Build Status](https://github.com/wtfo-guru/dailylog_lib/workflows/dailylog_lib/badge.svg)](https://github.com/wtfo-guru/dailylog/actions?query=workflow%3Adailylog_lib)
[![codecov](https://codecov.io/gh/wtfo-guru/dailylog-lib/branch/main/graph/badge.svg)](https://codecov.io/gh/wtfo-guru/dailylog-lib)
[![Python Version](https://img.shields.io/pypi/pyversions/dailylog-lib.svg)](https://pypi.org/project/dailylog-lib/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

## Overview

dailylog-lib is a minimal logger that will suppress all but first message in a specified
time to screen, while continuing to log messages to a specified log file.

## Installation

```bash

pip install dailylog-lib

```

## Usage

```bash
dailylog --help
Usage: dailylog [OPTIONS] COMMAND [ARGS]...

  Entry point for click script.

Options:
  -C, --cache TEXT        specify alternate cache file (default ~/.cache/dailylog.json)
  -c, --config TEXT       specify alternate config file (default ~/.config/dailylog.yaml)
  -d, --debug             increment debug level
  -t, --test / --no-test  specify test mode
  -v, --verbose           increment verbosity level
  -V, --version           show version and exit
  -h, --help              Show this message and exit.

Commands:
  log              Log an error.
  set-default-log  Set a new default log.
```

```bash
dailylog log --help
Usage: dailylog log [OPTIONS]

  Log a message.

Options:
  -k TEXT     Specify key  [required]
  -m TEXT     Specify message  [required]
  -s INTEGER  Specify seconds to suppress (default 86400 [one day])
  -l INTEGER  Specify one of logging levels (default: logging.ERROR)
  -f TEXT     Specify alternate log file
  -h, --help  Show this message and exit.
```

```bash
dailylog set-default-log --help
Usage: dailylog set-default-log [OPTIONS] LOG_FN

  Set a new default log.

Options:
  -h, --help  Show this message and exit.
```

## Documentation

- [Stable](https://dailylog-lib.readthedocs.io/en/stable)

- [Latest](https://dailylog-lib.readthedocs.io/en/latest)

## License

[MIT](https://github.com/wtfo-guru/dailylog-lib/blob/main/LICENSE)
