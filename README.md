# python-utils-24

A curated collection of high-performance Python helper functions designed to streamline repetitive development tasks. This library focuses on simplifying data serialization, file system operations, and execution timing to improve overall code maintainability.

## Features

*   **Robust File Operations:** Advanced wrappers for safe directory traversal, recursive file hashing, and automated cleanup routines.
*   **Performance Benchmarking:** Integrated decorator-based timers to measure execution duration and memory consumption with millisecond precision.
*   **Data Validation:** Lightweight utility suite for sanitizing dictionary inputs and enforcing schema consistency across complex JSON structures.
*   **Logging Enhancements:** Pre-configured handlers that enable color-coded terminal output and structured file rotation with zero boilerplate.

## Installation

Install the package directly via pip:

```bash
pip install python-utils-24
```

To include development dependencies for testing, run:

```bash
pip install python-utils-24[dev]
```

## Basic Usage

Import the required modules to access the utility suite. Below is an example of using the performance timer to profile a function:

```python
from pyutils24 import timer, file_manager

@timer
def process_data(data):
    # Perform intensive data transformation
    return [x**2 for x in data]

# Use file utilities to verify paths safely
if file_manager.exists('data/input.json'):
    result = process_data([1, 2, 3, 4, 5])
    print(f"Task completed successfully.")
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.