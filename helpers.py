import os
import shutil
from typing import List, Optional

def cleanup_temp_files(directory: str, extensions: Optional[List[str]] = None) -> int:
    """Remove temporary files from specified directory with optional extension filtering."""
    count = 0
    if not os.path.exists(directory):
        return count

    target_exts = extensions or ['.tmp', '.log', '.bak']

    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)
        if os.path.isfile(path):
            if any(path.endswith(ext) for ext in target_exts):
                os.remove(path)
                count += 1
    return count

def clear_directory_contents(directory: str) -> None:
    """Recursively remove all contents within a directory without deleting the root."""
    if not os.path.exists(directory):
        return

    for item in os.listdir(directory):
        path = os.path.join(directory, item)
        try:
            if os.path.isfile(path) or os.path.islink(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
        except OSError as e:
            print(f"Failed to delete {path}: {e}")

def ensure_clean_workspace(path: str) -> None:
    """Reset workspace by removing existing temp files and clearing content."""
    cleanup_temp_files(path)
    clear_directory_contents(path)