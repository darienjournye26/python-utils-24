import logging
import sys
from typing import Optional

def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    """Configures a logger with robust error handling for file IO."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Clear existing handlers to prevent duplicate logs
    if logger.hasHandlers():
        logger.handlers.clear()

    # Add console output
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # Add file output with edge case handling
    if log_file:
        try:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except (OSError, PermissionError) as e:
            logger.error(f"Failed to initialize log file {log_file}: {e}")
            # Fallback to console only if file access fails
            pass
            
    return logger

def safe_log(logger: logging.Logger, message: str, level: str = 'info') -> None:
    """Logs messages safely avoiding attribute errors."""
    log_func = getattr(logger, level.lower(), logger.info)
    try:
        log_func(message)
    except Exception as e:
        # Ensure logging failures do not crash the application
        sys.stderr.write(f"Logging failed: {e}\n")