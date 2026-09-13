import logging
import sys
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import Optional

DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DEFAULT_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logger(
    name: str = "app",
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,
    backup_count: int = 5,
    log_format: str = DEFAULT_LOG_FORMAT,
    console_output: bool = True,
) -> logging.Logger:
    """Configure and return a logger instance with rotating file support."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Clear existing handlers to prevent duplicate logging
    if logger.hasHandlers():
        logger.handlers.clear()

    formatter = logging.Formatter(fmt=log_format, datefmt=DEFAULT_DATE_FORMAT)

    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)

        file_handler = RotatingFileHandler(
            filename=log_path,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
