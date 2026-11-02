import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standard formatted logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger

def log_execution_time(logger: logging.Logger, func_name: str, duration: float) -> None:
    """Utility for logging function performance metrics."""
    logger.info(f"Execution of {func_name} took {duration:.4f} seconds")

def setup_debug_mode(logger: logging.Logger) -> None:
    """Forces logger to debug level for diagnostics."""
    logger.setLevel(logging.DEBUG)
    for handler in logger.handlers:
        handler.setLevel(logging.DEBUG)