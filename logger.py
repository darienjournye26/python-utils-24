import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standard logger instance."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

def log_exception(logger: logging.Logger, message: str, exc: Exception) -> None:
    """Helper to format and log exceptions consistently."""
    logger.error(f"{message}: {type(exc).__name__} - {str(exc)}", exc_info=True)

def setup_basic_logging(level: int = logging.INFO) -> None:
    """Initialize root logging configuration."""
    logging.basicConfig(
        level=level,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )