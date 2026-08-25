import logging
from logging.handlers import RotatingFileHandler
import os

def setup_rotating_logger(
    name: str = "python-utils",
    log_file: str = "app.log",
    level: int = logging.INFO,
    max_bytes: int = 1024 * 1024 * 10,  # 10 MB
    backup_count: int = 5
) -> logging.Logger:
    """Configure and return a logger with file rotation.

    Uses RotatingFileHandler to prevent log files from growing indefinitely.
    """
    logger = logging.getLogger(name)
    # Prevent adding handlers multiple times
    if logger.hasHandlers():
        return logger
    logger.setLevel(level)
    # Create log directory if needed
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    # Rotating file handler
    file_handler = RotatingFileHandler(
        log_file, maxBytes=max_bytes, backupCount=backup_count
    )
    file_handler.setLevel(level)
    file_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )
    file_handler.setFormatter(file_format)
    logger.addHandler(file_handler)
    # Add stream handler for console output
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(level)
    stream_format = logging.Formatter("%(levelname)s: %(message)s")
    stream_handler.setFormatter(stream_format)
    logger.addHandler(stream_handler)
    return logger

# Example of usage (for testing the module)
if __name__ == "__main__":
    logger = setup_rotating_logger()
    logger.info("Logger setup complete with rotation enabled.")
    logger.warning("This is a test warning message.")
    logger.error("This is a test error message.")