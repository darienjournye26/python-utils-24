# python-utils-24

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A lightweight, zero-dependency Python library designed to streamline common data manipulation, file handling, and logging tasks. It provides a highly optimized set of helper functions to accelerate daily development workflows without bloating your environment.

## Features

* **Smart File I/O:** Safe JSON and CSV wrappers with automatic directory creation and reliable fallback mechanisms.
* **Decorators for Devs:** Production-ready retry logic and execution-time profilers for instant performance debugging.
* **Collection Helpers:** Fast deep-merging of nested dictionaries and memory-efficient generator-based list chunking.
* **Ready-to-use Logging:** A pre-configured console and file logger requiring only a single line of setup.

## Installation

Install the package directly from PyPI:

```bash
pip install python-utils-24
```

## Quick Start

Here is a quick example of how to load nested configurations safely and log the output:

```python
from python_utils_24.io import safe_load_json
from python_utils_24.logger import setup_logger

logger = setup_logger("AppLogger")

# Safely load JSON config, returning a default fallback if the file is missing or corrupt
config = safe_load_json("config/settings.json", default={"port": 8080})
logger.info(f"Server started on port: {config['port']}")
```

## License

Distributed under the MIT License. See `LICENSE` for