from typing import Any, Hashable, Sequence, Union

def get_nested_value(
    data: Any,
    path: Union[str, Sequence[Hashable]],
    default: Any = None,
    separator: str = "."
) -> Any:
    """
    Safely retrieve nested values from mixed dict/list structures.

    Handles edge cases like out-of-bound indices, type mismatches,
    invalid keys, and non-container objects smoothly.
    """
    if not path:
        return data if data is not None else default

    # Normalize path keys
    if isinstance(path, str):
        keys = path.split(separator) if separator else [path]
    else:
        keys = list(path)

    current = data
    for key in keys:
        if current is None:
            return default

        # Handle dictionary access
        if isinstance(current, dict):
            try:
                if key in current:
                    current = current[key]
                else:
                    return default
            except TypeError:
                # Key is not hashable
                return default

        # Handle sequence access (list/tuple)
        elif isinstance(current, (list, tuple)):
            try:
                idx = int(key)
                if -len(current) <= idx < len(current):
                    current = current[idx]
                else:
                    return default
            except (ValueError, TypeError):
                return default

        # Handle non-container nodes
        else:
            return default

    return current


def safe_convert(value: Any, target_type: type, default: Any = None) -> Any:
    """
    Safely convert value to target_type, returning default on any failure.
    """
    if value is None:
        return default
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default
