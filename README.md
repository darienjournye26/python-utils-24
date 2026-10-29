# python-utils-24

`python-utils-24` is a collection of high-performance utility functions designed to streamline routine Python development tasks. It focuses on reducing boilerplate code for data manipulation, file system operations, and environment management.

## Features

*   **Robust File Operations:** Enhanced wrappers for recursive directory traversal and intelligent file searching with pattern matching.
*   **Performance Profiling:** Lightweight decorators for tracking function execution time and memory usage with minimal overhead.
*   **Data Validation:** A suite of type-safe helpers for parsing complex nested dictionaries and enforcing strict JSON schema integrity.
*   **System Helpers:** Cross-platform utilities to retrieve system hardware specs and manage persistent environment configurations.

## Installation

Install the package via `pip`:

```bash
pip install python-utils-24
```

For development mode:

```bash
git clone https://github.com/Developer/python-utils-24.git
cd python-utils-24
pip install -e .
```

## Usage

Import the desired module and utilize the optimized wrappers. Here is a quick example of the profiling decorator:

```python
from pyutils24.decorators import profile_time

@profile_time
def process_data(data):
    # Simulate heavy workload
    return [i**2 for i in data]

result = process_data(range(1000000))
# Output: Function 'process_data' executed in 0.084 seconds.
```

## License

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.