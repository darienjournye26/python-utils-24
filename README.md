# python-utils-24

A curated collection of production-ready Python utility functions designed to streamline daily development tasks. This library focuses on performance, readability, and minimizing boilerplate code for common data manipulation and system operations.

## Features

*   **Robust File Operations:** Simplified wrappers for recursive directory traversal and atomic file writing with automated backups.
*   **Performance Decorators:** Lightweight decorators for function execution timing and memory-efficient caching strategies.
*   **Data Validation:** A flexible set of schema-less validation helpers for nested JSON structures and environment variables.
*   **String Sanitization:** Optimized text cleaning utilities for handling irregular whitespace, Unicode normalization, and pattern-based redaction.

## Installation

Install the package via pip:

```bash
pip install python-utils-24
```

For development or local testing, clone the repository and install dependencies:

```bash
git clone https://github.com/Developer/python-utils-24.git
cd python-utils-24
pip install -r requirements.txt
```

## Usage

Easily integrate core utilities into your scripts to reduce repetitive code:

```python
from pyutils24.file_ops import atomic_write
from pyutils24.decorators import time_execution

@time_execution
def process_data(data):
    # Process your data efficiently
    return [d.strip().lower() for d in data]

# Write to file safely
atomic_write("output.txt", "Task completed successfully.")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.