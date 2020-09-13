# polf

[![PyPI][pypi-image]][pypi-link]
[![PyPI Python versions][pypi-versions-image]][pypi-link]
[![License][license-image]][license-link]
[![Tests][tests-image]][tests-link]
[![Documentation status][doc-image]][doc-link]

Simple library written with the Python C API to calculate points on lines.
It does not perform any checks on the passed data, but rather follows the
GIGO processing pattern.

I have written it with the main purpose of learning, but it may be useful in
some situation or it can serve as a reference to get you started in the
Python C API. If it has been useful to you, do not hesitate to leave a star.

## Install

```
pip install polf
```

## Useful links

- [Documentation on ReadTheDocs][doc-link]
- [Issue tracker][issue-tracker-link]

## Contributing (Linux)

First, create a virtual environment and initialize it with:

```
python3 -m virtualenv venv
source venv/bin/activate
```

### Develop commands

- Build documentation: `make docs`
- Run tests: `make tests`
- Lint: `make lint`

[pypi-image]: https://img.shields.io/pypi/v/polf
[pypi-link]: https://pypi.org/project/polf/
[pypi-versions-image]: https://img.shields.io/pypi/pyversions/polf?logo=python&logoColor=aaaaaa&labelColor=333333
[license-image]: https://img.shields.io/pypi/l/polf?color=light-green
[license-link]: https://github.com/mondeja/polf/blob/master/LICENSE
[tests-image]: https://github.com/mondeja/cpolf/workflows/polf/badge.svg
[tests-link]: https://github.com/mondeja/cpolf/actions?query=workflow%3Apolf
[doc-image]: https://readthedocs.org/projects/polf/badge/?version=latest
[doc-link]: https://polf.readthedocs.io
[issue-tracker-link]: https://github.com/mondeja/cpolf/issues

