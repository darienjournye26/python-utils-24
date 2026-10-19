# python-utils-24

A curated collection of production-ready Python utility functions designed to streamline daily development tasks. This library focuses on performance, type safety, and minimizing boilerplate code for common engineering challenges.

## Features

*   **Data Transformation:** Robust serialization helpers for nested dictionaries and high-performance JSON processing.
*   **Time Utilities:** Simplified timezone-aware conversions and human-readable duration formatting.
*   **File I/O:** Streamlined context managers for batch file processing with built-in checksum verification.
*   **Type-Safe Helpers:** A set of strict validators and data-sanitization patterns for consistent API request handling.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-24
```

For local development or manual installation, clone the repository and run:

```bash
git clone https://github.com/Developer/python-utils-24.git
cd python-utils-24
pip install -e .
```

## Usage

Easily integrate shared utilities into your existing workflow:

```python
from pyutils import time_format, file_manager

# Convert seconds to human-readable strings
uptime = time_format.to_human(3665) 
print(f"Server Uptime: {uptime}")

# Safely read and sanitize JSON data
data = file_manager.read_json("config.json", validate=True)
print(data.get("api_key"))
```

## Contributing

We welcome contributions! Please open an issue to discuss proposed changes or submit a pull request for existing features. Ensure all new code adheres to the [PEP 8](https://www.python.org/dev/peps/pep-0008/) standard and includes accompanying unit tests.

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Distributed under the MIT License. See `LICENSE` for more information.