import os
import logging
from logging.handlers import RotatingFileHandler
from typing import Optional


def setup_logger(
    name: str = "app",
    log_file: Optional[str] = "app.log",
    level: int = logging.INFO,
    max_bytes: int = 5 * 1024 * 1024,  # 5 MB
    backup_count: int = 5,
    fmt: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
) -> logging.Logger:
    """Configures and returns a logger instance with optional rotating file output."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if logger.handlers:
        return logger

    formatter = logging.Formatter(fmt)

    # Console handler output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Rotating file handler configuration
    if log_file:
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=backup_count,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def get_logger(name: str = "app") -> logging.Logger:
    """Retrieve an existing logger or initialize a default setup."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        return setup_logger(name)
    return logger
