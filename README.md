# python-utils-24

A curated collection of production-ready Python utility functions designed to streamline daily development tasks. This library focuses on performance, type safety, and minimizing boilerplate code for common data manipulation and system operations.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Features

*   **Type-Safe Converters:** Robust functions to handle complex dictionary-to-object mapping and nested data structure serialization.
*   **Performance Decorators:** Lightweight decorators for memoization, execution timing, and asynchronous retry logic with exponential backoff.
*   **Path & IO Helpers:** Simplified wrappers for cross-platform file system operations, recursive directory scanning, and bulk file processing.
*   **Validation Suite:** A compact set of validators for common string patterns, email formats, and custom data constraints.

## Installation

Install the package via pip:

```bash
pip install python-utils-24
```

To include development dependencies for testing and linting:

```bash
pip install python-utils-24[dev]
```

## Basic Usage

Import the utilities directly into your workflow to reduce redundancy:

```python
from pyutils24.decorators import time_execution
from pyutils24.files import get_files_by_extension

# Time any function call automatically
@time_execution
def process_data(data):
    return [d.upper() for d in data]

# Recursively find all log files in a directory
logs = get_files_by_extension('./logs', 'log')

print(f"Found {len(logs)} log files.")
process_data(['alpha', 'beta', 'gamma'])
```

## Contributing

Contributions are welcome. Please open an issue to discuss proposed changes or submit a pull request for bug fixes. Ensure all new functions include type hints and corresponding tests in the `tests/` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.