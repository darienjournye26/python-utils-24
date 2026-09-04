# python-utils-24

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

`python-utils-24` is a lightweight, zero-dependency suite of helper modules designed to simplify daily Python development tasks. It eliminates repetitive boilerplate code by providing optimized wrappers for file handling, string manipulation, and function execution.

## Features

- **Smart File Operations:** Safe JSON and YAML loaders with built-in fallback defaults and atomic file writes.
- **Text & String Processing:** Fast slugification, Unicode normalization, and pattern-matching utilities.
- **Execution Decorators:** Ready-to-use decorators for function timing, automatic retries with exponential backoff, and result caching.
- **Environment Management:** Light parser for `.env` files with automatic type casting for booleans, integers, and lists.

## Installation

Install the package directly via `pip`:

```bash
pip install python-utils-24
```

Or install from the repository:

```bash
git clone https://github.com/Developer/python-utils-24.git
cd python-utils-24
pip install .
```

## Quick Start

```python
from python_utils_24.files import safe_json_load
from python_utils_24.strings import slugify
from python_utils_24.decorators import retry

# 1. Clean string transformation
clean_slug = slugify("Python Utils 2024 Release!")
print(clean_slug)  # Output: "python-utils-2024-release"

# 2. Safe file loading with fallbacks
config = safe_json_load("settings.json", default={"theme": "dark", "debug": False})

# 3. Flaky task retries with backoff
@retry(tries=3, delay=1.5)
def process_network_request():
    # Function logic here
    return True

process_network_request()
```

## License

This project is licensed under the [MIT License](LICENSE).