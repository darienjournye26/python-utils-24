from typing import Any, Dict, List, Optional


def clean_nested_dict(data: Dict[str, Any], keys_to_strip: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Recursively removes specified keys from a dictionary and cleans null values.
    """
    if keys_to_strip is None:
        keys_to_strip = []

    cleaned = {}
    for key, value in data.items():
        if key in keys_to_strip:
            continue

        if isinstance(value, dict):
            cleaned[key] = clean_nested_dict(value, keys_to_strip)
        elif isinstance(value, list):
            cleaned[key] = [
                clean_nested_dict(i, keys_to_strip) if isinstance(i, dict) else i
                for i in value
            ]
        elif value is not None:
            cleaned[key] = value

    return cleaned


def batch_process(items: List[Any], batch_size: int = 10) -> List[List[Any]]:
    """
    Splits an input list into smaller chunks for batch operations.
    """
    if batch_size <= 0:
        raise ValueError("batch_size must be a positive integer")

    return [items[i:i + batch_size] for i in range(0, len(items), batch_size)]
