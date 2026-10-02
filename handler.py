from typing import Any, Dict, List, Union


def get_by_path(
    data: Union[Dict[str, Any], List[Any]],
    path: str,
    delimiter: str = ".",
    default: Any = None,
) -> Any:
    """Retrieve a nested value from a dict or list using a delimited path.

    Example:
        get_by_path({'a': {'b': [10, 20]}}, 'a.b.1') -> 20
    """
    if not path:
        return data

    parts = path.split(delimiter)
    current = data

    for part in parts:
        if isinstance(current, dict):
            if part in current:
                current = current[part]
            else:
                return default
        elif isinstance(current, list):
            try:
                index = int(part)
                current = current[index]
            except (ValueError, IndexError):
                return default
        else:
            return default

    return current


def flatten_dict(
    d: Dict[str, Any], parent_key: str = "", delimiter: str = "."
) -> Dict[str, Any]:
    """Flatten a nested dictionary into a single-level dictionary.

    Example:
        flatten_dict({'a': {'b': 1}}) -> {'a.b': 1}
    """
    items: List[tuple] = []
    for k, v in d.items():
        new_key = f"{parent_key}{delimiter}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, delimiter=delimiter).items())
        else:
            items.append((new_key, v))
    return dict(items)
