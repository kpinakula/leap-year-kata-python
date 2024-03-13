# Python kata starter

This is a starter repository for doing katas in Python.

It uses [Poetry](https://python-poetry.org/) for dependency management and [Pytest](https://pytest.org/) for running tests.

## Pre-requisites

* Python 3.8+
* Poetry

## Getting started

Run `make install` to get all dependencies installed

## Linting

Code formatting can be done using [Black](https://black.readthedocs.io/).

To lint and auto format all files
```
make lint
```

To check formatting of all files
```
make check
```

## Running tests

To run all tests
```
make test
```

To run all tests in watch mode
```
make test-watch
```

## The Kata

A leap year is defined as one that is divisible by 4, but is not otherwise divisible by 100 unless it is also divisible by 400.

For example:

- 2001 is a typical common year
- 1996 is a typical leap year
- 1900 is an atypical common year
- 2000 is an atypical leap year
