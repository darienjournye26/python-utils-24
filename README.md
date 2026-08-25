# python-utils-24

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

python-utils-24 is a lightweight collection of Python utilities aimed at streamlining routine development tasks across various projects. It delivers reliable helpers for file system operations, function resilience, and data presentation without introducing heavy dependencies.

## Features

- Recursive directory creation with automatic permission handling
- Retry decorator for handling transient failures in I/O or network calls
- Human-readable byte size formatting with support for SI and IEC units
- Simple config merger that combines JSON files with environment variables

## Installation

```bash
pip install python-utils-24
```

## Usage

```python
from python_utils_24 import ensure_dir, format_size
from python_utils_24.decorators import retry

ensure_dir("data/exports")

@retry(attempts=3, delay=0.5)
def fetch_data():
    # network or file operation
    pass

print(format_size(1536000))  # 1.5 MB
```