import logging
import sys
from typing import Optional

class AppLogger:
    """Standardized logging configuration for python-utils-24"""
    
    def __init__(self, name: str, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self._setup_handler()

    def _setup_handler(self) -> None:
        """Configure console stream handler with formatting"""
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler = logging.StreamHandler(sys.stdout)
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def info(self, msg: str) -> None:
        self.logger.info(msg)

    def error(self, msg: str, exc_info: bool = False) -> None:
        self.logger.error(msg, exc_info=exc_info)

def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Factory function for consistent logger instantiation"""
    return AppLogger(name, level).logger