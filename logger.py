import logging
import sys
from typing import Optional, Union, Dict


class CustomFormatter(logging.Formatter):
    """Custom logging formatter that adds simple color-coding for terminal output."""

    grey = "\u001b[38;20m"
    yellow = "\u001b[33;20m"
    red = "\u001b[31;20m"
    bold_red = "\u001b[31;1m"
    reset = "\u001b[0m"
    log_format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS: Dict[int, str] = {
        logging.DEBUG: grey + log_format + reset,
        logging.INFO: grey + log_format + reset,
        logging.WARNING: yellow + log_format + reset,
        logging.ERROR: red + log_format + reset,
        logging.CRITICAL: bold_red + log_format + reset,
    }

    def format(self, record: logging.LogRecord) -> str:
        """Formats the log record with color depending on the log level."""
        log_fmt = self.FORMATS.get(record.levelno, self.log_format)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def get_logger(
    name: str,
    level: Union[int, str] = logging.INFO,
    filepath: Optional[str] = None,
) -> logging.Logger:
    """Configures and retrieves a standardized logger instance.

    Args:
        name: The name of the logger, typically __name__.
        level: The logging level (e.g., logging.INFO or 'INFO').
        filepath: Optional file path to write log output to.

    Returns:
        A pre-configured logging.Logger instance.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(level)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(CustomFormatter())
    logger.addHandler(console_handler)

    if filepath:
        file_handler = logging.FileHandler(filepath, encoding="utf-8")
        file_handler.setLevel(level)
        file_formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)

    return logger
