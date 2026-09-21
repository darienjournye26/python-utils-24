import re
from typing import Any, Dict, Generator, List, Optional


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", sep: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else str(k)
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def chunk_iterable(
    iterable: List[Any], chunk_size: int
) -> Generator[List[Any], None, None]:
    """Yield successive chunks of specified size from a list."""
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i : i + chunk_size]


def safe_get(
    data: Dict[str, Any], key_path: str, default: Optional[Any] = None
) -> Any:
    """Safely retrieve nested values from a dictionary using dot notation."""
    keys = key_path.split(".")
    current = data
    for k in keys:
        if isinstance(current, dict) and k in current:
            current = current[k]
        else:
            return default
    return current


def slugify(text: str) -> str:
    """Convert string into a normalized URL and filename friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[-\s]+", "-", text)
