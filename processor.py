from typing import Any, Dict, List, Optional

def flatten_data(data: Any, parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flattens a nested dictionary into a single-level dictionary.
    Uses recursive traversal to concatenate keys with the specified separator.
    """
    items: List[tuple] = []
    if isinstance(data, dict):
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten_data(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
    else:
        return {parent_key: data}
    return dict(items)

def sanitize_keys(data: Dict[str, Any], prefix: str = 'clean_') -> Dict[str, Any]:
    """
    Normalizes dictionary keys by removing non-alphanumeric characters
    and applying a standardized prefix for data consistency.
    """
    sanitized = {}
    for key, value in data.items():
        clean_key = ''.join(c if c.isalnum() else '_' for c in str(key))
        sanitized[f"{prefix}{clean_key.strip('_')}"] = value
    return sanitized

def batch_process(items: List[Any], func: callable, chunk_size: int = 10) -> List[Any]:
    """
    Processes list items in defined chunks to prevent
    memory exhaustion with large datasets.
    """
    results = []
    for i in range(0, len(items), chunk_size):
        chunk = items[i:i + chunk_size]
        results.extend([func(item) for item in chunk])
    return results