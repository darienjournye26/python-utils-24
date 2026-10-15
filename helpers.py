import os
import shutil
from pathlib import Path
from typing import Union, List

def clean_temp_directories(path: Union[str, Path], extension: str = '.tmp') -> int:
    """Removes files with specific extension from directory."""
    target_dir = Path(path)
    if not target_dir.is_dir():
        return 0

    count = 0
    for item in target_dir.glob(f'*{extension}'):
        try:
            if item.is_file():
                item.unlink()
                count += 1
        except OSError:
            continue
    return count

def ensure_directory(path: Union[str, Path]) -> None:
    """Creates directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def format_byte_size(size_bytes: int) -> str:
    """Converts bytes to human readable format."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} TB"

def get_directory_tree(path: Union[str, Path]) -> List[str]:
    """Lists all files in directory recursively."""
    return [str(p) for p in Path(path).rglob('*') if p.is_file()]