from typing import Any, Dict, List, Optional

def flatten_dict(data: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, Any]:
    """Flatten a nested dictionary into a flat dictionary.
    Useful for general data handling in processing pipelines.
    """
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            for i, item in enumerate(v):
                if isinstance(item, dict):
                    items.extend(flatten_dict(item, f"{new_key}{sep}{i}", sep=sep).items())
                else:
                    items.append((f"{new_key}{sep}{i}", item))
        else:
            items.append((new_key, v))
    return dict(items)

def safe_get_nested(data: Dict[str, Any], path: str, default: Any = None, sep: str = '.') -> Any:
    """Safely retrieve a value from nested dictionary using dot-separated path.
    Handles missing keys by returning default.
    """
    keys = path.split(sep)
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

def filter_and_transform(data: List[Dict[str, Any]], filter_key: str, filter_value: Any, transform_key: Optional[str] = None) -> List[Any]:
    """Filter list of dictionaries and optionally extract specific keys.
    Practical for general data handling tasks.
    """
    filtered = [item for item in data if item.get(filter_key) == filter_value]
    if transform_key:
        return [item.get(transform_key) for item in filtered]
    return filtered

def batch_process(data: List[Any], batch_size: int = 10) -> List[List[Any]]:
    """Split data into batches for processing.
    Helps in handling large datasets generally.
    """
    return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
