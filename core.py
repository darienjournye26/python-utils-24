from typing import Dict, Any


def flatten_dict(d: Dict[str, Any], parent_key: str = "", sep: str = "_") -> Dict[str, Any]:
    """
    Recursively flattens a nested dictionary into a single-level dictionary.

    Keys in the resulting dictionary are concatenated using the specified separator.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def unflatten_dict(d: Dict[str, Any], sep: str = "_") -> Dict[str, Any]:
    """
    Recreates a nested dictionary structure from a flattened dictionary.

    Assumes the flat dictionary keys were constructed using the specified separator.
    """
    result: Dict[str, Any] = {}
    for flat_key, value in d.items():
        parts = flat_key.split(sep)
        current = result
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            current = current[part]
        current[parts[-1]] = value
    return result
