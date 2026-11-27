from typing import Any, Dict, List, Optional

def deep_flatten(items: List[Any], separator: str = '.') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single-level dictionary."""
    items_flat = {}

    def _recurse(current: Any, prefix: str = '') -> None:
        if isinstance(current, dict):
            for key, value in current.items():
                new_key = f"{prefix}{separator}{key}" if prefix else key
                _recurse(value, new_key)
        elif isinstance(current, list):
            for i, value in enumerate(current):
                _recurse(value, f"{prefix}{separator}{i}")
        else:
            items_flat[prefix] = current

    _recurse(items)
    return items_flat

def sanitize_data(data: Dict[str, Any], keys_to_mask: Optional[List[str]] = None) -> Dict[str, Any]:
    """Removes sensitive keys from a dictionary based on a provided list."""
    if not keys_to_mask:
        return data

    return {k: ('***' if k in keys_to_mask else v) for k, v in data.items()}

def batch_process(data: List[Any], batch_size: int) -> List[List[Any]]:
    """Chunks a list into smaller sub-lists of a specified size."""
    if batch_size <= 0:
        raise ValueError("batch_size must be a positive integer")
    
    return [data[i : i + batch_size] for i in range(0, len(data), batch_size)]