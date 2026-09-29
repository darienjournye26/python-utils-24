from typing import Any, Dict, List, Union

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """Flattens nested dictionary into single level structure."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def sanitize_list(data: List[Any]) -> List[Any]:
    """Removes None values and strips strings from list."""
    return [
        item.strip() if isinstance(item, str) else item 
        for item in data 
        if item is not None
    ]

def batch_process(data: List[Any], batch_size: int) -> List[List[Any]]:
    """Splits large list into manageable smaller chunks."""
    if batch_size <= 0:
        raise ValueError("batch_size must be positive")
    return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]