import logging
import sys
from typing import Optional

class AppLogger:
    """Standardized application logger for python-utils-24"""
    
    def __init__(self, name: str = "app_logger", level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        if not self.logger.handlers:
            handler = logging.StreamHandler(sys.stdout)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc_info: bool = False) -> None:
        self.logger.error(msg, exc_info=exc_info)

    def warning(self, msg: str) -> None:
        self.logger.warning(msg)

def get_logger(name: str = "default", level: int = logging.INFO) -> logging.Logger:
    """Factory function for consistent logging instances"""
    instance = AppLogger(name, level)
    return instance.logger