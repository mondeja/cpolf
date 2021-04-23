# polf

[![PyPI][pypi-image]][pypi-link]
[![PyPI Python versions][pypi-versions-image]][pypi-link]
[![License][license-image]][license-link]
[![Documentation status][doc-image]][doc-link]
[![Tests][tests-image]][tests-link]
[![Wheels][wheels-image]][wheels-link]

Simple library written with the Python C API to calculate points on lines.
It does not perform any checks on the passed data, but rather follows the
GIGO processing pattern.

I have written it with the main purpose of learning, but it may be useful in
some situation or it can serve as a reference to get you started in the
Python C API and building multiplatform wheels using
[cibuildwheel][cibuildwheel-link] and Github Actions. If it has been useful
to you, do not hesitate to leave a star.

## Install

```
pip install polf
```

## Useful links

- [Documentation on ReadTheDocs][doc-link]
- [Issue tracker][issue-tracker-link]

## Contributing (Linux)

Create a virtual environment, initialize it and install development dependencies:

```
python -m virtualenv venv
source venv/bin/activate
python -m pip install -e .[dev]
pre-commit install
```

[pypi-image]: https://img.shields.io/pypi/v/polf
[pypi-link]: https://pypi.org/project/polf/
[pypi-versions-image]: https://img.shields.io/pypi/pyversions/polf?logo=python&logoColor=aaaaaa&labelColor=333333
[license-image]: https://img.shields.io/pypi/l/polf?color=light-green
[license-link]: https://github.com/mondeja/polf/blob/master/LICENSE
[tests-image]: https://github.com/mondeja/cpolf/workflows/Test/badge.svg
[tests-link]: https://github.com/mondeja/cpolf/actions?query=event%3Apush
[doc-image]: https://readthedocs.org/projects/polf/badge/?version=latest
[doc-link]: https://polf.readthedocs.io
[issue-tracker-link]: https://github.com/mondeja/cpolf/issues
[wheels-image]: https://github.com/mondeja/cpolf/workflows/Build%20wheels/badge.svg
[wheels-link]: https://github.com/mondeja/cpolf/actions?query=event%3Arelease+
[cibuildwheel-link]: https://github.com/joerick/cibuildwheel
