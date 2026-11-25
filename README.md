# python-utils-24

`python-utils-24` is a curated collection of high-performance Python utilities designed to streamline daily automation and data processing tasks. This library focuses on providing robust, dependency-minimal solutions for common boilerplate code encountered in medium-to-large scale applications.

## Features

*   **File Orchestration:** Advanced file system utilities for recursive batch renaming, directory syncing, and memory-efficient log parsing.
*   **Data Validation:** A lightweight set of decorators for schema-less data integrity checks and runtime type enforcement.
*   **Async Batching:** Specialized throttled executors that allow for rate-limited execution of asynchronous IO-bound operations.
*   **Time Utilities:** Enhanced datetime helpers for human-readable relative time conversion and business-day arithmetic.

## Installation

Install the package directly from PyPI using pip:

```bash
pip install python-utils-24
```

For development installations, clone the repository and run:

```bash
git clone https://github.com/Developer/python-utils-24.git
cd python-utils-24
pip install -e .
```

## Basic Usage

The following example demonstrates how to use the built-in `ThrottledExecutor` to manage asynchronous network requests without overwhelming the target server:

```python
from python_utils.async_tools import ThrottledExecutor
import asyncio

async def fetch_data(item):
    return f"Processed {item}"

async def main():
    executor = ThrottledExecutor(limit=5)
    items = range(20)
    
    results = await executor.run_map(fetch_data, items)
    print(results)

asyncio.run(main())
```

## License

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Distributed under the MIT License. See `LICENSE` for more information.