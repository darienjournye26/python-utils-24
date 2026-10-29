import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """
    Creates and configures a standard logger instance.

    Args:
        name: The name of the logger module.
        level: The logging threshold level.

    Returns:
        A configured logging.Logger instance.
    """
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

def log_exception(logger: logging.Logger, message: str, exc: Optional[Exception] = None) -> None:
    """
    Logs an error message along with optional exception details.

    Args:
        logger: The logger instance to use.
        message: The custom error message to log.
        exc: The exception object if applicable.
    """
    if exc:
        logger.error(f"{message}: {str(exc)}", exc_info=True)
    else:
        logger.error(message)