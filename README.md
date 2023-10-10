# django-thailand-geography

[![GitHub](https://img.shields.io/github/license/earthpyy/django-thailand-geography)](https://github.com/earthpyy/django-thailand-geography/blob/main/LICENSE)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/earthpyy/django-thailand-geography/ci.yml?branch=main)](https://github.com/earthpyy/django-thailand-geography/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/earthpyy/django-thailand-geography/branch/main/graph/badge.svg?token=PN19DJ3SDF)](https://codecov.io/gh/earthpyy/django-thailand-geography)
[![PyPI](https://img.shields.io/pypi/v/django-nats-client)](https://pypi.org/project/django-nats-client/)  
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-nats-client)](https://github.com/earthpyy/django-thailand-geography)

## Installation

```bash
pip install django-thailand-geography
```

## Setup

1. Add `thailand_geography` into `INSTALLED_APPS`

   ```python
   # settings.py

   INSTALLED_APPS = [
       ...
       'thailand_geography',
   ]
   ```

## Development

### Requirements

- Docker
- Python
- Poetry

### Linting

```bash
make lint
```

### Testing

```bash
make test
```

### Fix Formatting

```bash
make yapf
```
