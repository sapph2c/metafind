# Metafind

![Python Version from PEP 621 TOML](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Fsapph2c%2Fexifool%2Fmain%2Fpyproject.toml&style=for-the-badge&logo=python&logoSize=auto)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/sapph2c/exifool/ci.yml?style=for-the-badge&logo=github&logoSize=auto)
![GitHub deployments](https://img.shields.io/github/deployments/sapph2c/exifool/pypi?style=for-the-badge&logo=pypi&logoColor=white&logoSize=auto)

**Metafind** is a metadata analysis tool written for CSEC-473 - Penetration Testing.

Currently `exiftool` is the only supported backend, but there are plans in the future to add additional backends.

## Features

- CLI output that displays a list of files and their metadata.
- Displays an alphabetized list of all metadata elements contained in the files.
- Attempts to scrub files of all metadata.

## Install

Metafind is available as a python package on PyPi:

```
pip install metafind
```

## Usage

CLI options:

```
metafind --help

Usage: exifool [OPTIONS]

  ___________      .__  _____             .__
  \_   _____/__  __|__|/ ____\____   ____ |  |
  |     __)_\  \/  /  \   __\/  _ \ /  _ \|  |
  |         \>    <|  ||  | (  <_> |  <_> )  |__
  /_______  /__/\_ \__||__|  \____/ \____/|____/
          \/      \/

  Written with ❤️ by sapph2c

  Metadata analysis tool written for CSEC-473

Options:
  --path TEXT  Path to the file to perform metadata analysis on.
  --help       Show this message and exit.

```



```bash
metafind --path example.pdf
```

Sample output:

```bash
```
