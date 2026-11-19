import typing
from typing import Any, Iterable, Dict, List

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flatten a nested dictionary using a separator."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_list(data: Iterable[Any], size: int) -> List[List[Any]]:
    """Split an iterable into fixed-size chunks."""
    data_list = list(data)
    return [data_list[i : i + size] for i in range(0, len(data_list), size)]

def safe_get(data: Dict[Any, Any], keys: Iterable[str], default: Any = None) -> Any:
    """Access nested dictionary values safely."""
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return default