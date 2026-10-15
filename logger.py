import logging
import sys
from typing import Optional

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures and returns a standardized console logger."""
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

def log_exception(logger: logging.Logger, e: Exception, message: Optional[str] = None) -> None:
    """Logs an exception with an optional context message."""
    context = f"{message}: " if message else ""
    logger.error(f"{context}{type(e).__name__}: {str(e)}", exc_info=True)

class LoggerMixin:
    """Mixin to provide a logger instance to classes."""
    @property
    def logger(self) -> logging.Logger:
        return get_logger(self.__class__.__name__)