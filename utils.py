from typing import Any, Iterable, Dict, List, Optional

def chunk_data(data: Iterable[Any], size: int) -> List[List[Any]]:
    """Splits an iterable into smaller chunks of a fixed size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer")
    
    items = list(data)
    return [items[i:i + size] for i in range(0, len(items), size)]

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens a nested dictionary into a single level."""
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_input(data: Any, default: Any = None) -> Any:
    """Returns data if not None, otherwise returns the default value."""
    return data if data is not None else default