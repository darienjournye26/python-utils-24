import logging
import sys
from typing import Optional

def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Configures a robust logger instance with basic error handling."""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    try:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        if not logger.handlers:
            logger.addHandler(handler)
    except (OSError, ValueError) as e:
        # Fallback to null logging if output stream initialization fails
        return logging.getLogger('null_logger')

    return logger

def safe_log(logger: logging.Logger, message: str, level: str = 'info') -> None:
    """Logs messages while protecting against serialization errors."""
    log_map = {
        'info': logger.info,
        'error': logger.error,
        'warning': logger.warning
    }
    
    log_func = log_map.get(level.lower(), logger.info)
    
    try:
        if not isinstance(message, str):
            message = str(message)
        log_func(message)
    except Exception as e:
        # Prevention of cascading failures in logging system
        sys.stderr.write(f"Logging failure: {str(e)}\n")
