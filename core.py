from typing import Any, List, Optional, Union


def safe_get(
    data: Any,
    key_path: str,
    default: Any = None,
    delimiter: str = "."
) -> Any:
    """Safely retrieve nested values from data structures with edge case handling."""
    if not key_path or not isinstance(key_path, str):
        return default

    keys = key_path.split(delimiter)
    current = data

    for key in keys:
        if current is None:
            return default

        if isinstance(current, dict):
            current = current.get(key, default)
        elif isinstance(current, (list, tuple)):
            try:
                index = int(key)
                if 0 <= index < len(current):
                    current = current[index]
                else:
                    return default
            except (ValueError, TypeError):
                return default
        else:
            return default

    return current if current is not default else default


def safe_cast(
    value: Any,
    target_type: type,
    default: Any = None
) -> Any:
    """Cast a value to a target type with safe error handling for bad inputs."""
    if value is None:
        return default

    try:
        # Edge case: converting float-like strings directly to int
        if target_type is int and isinstance(value, str):
            return int(float(value))
        return target_type(value)
    except (ValueError, TypeError, OverflowError):
        return default


def safe_divide(
    numerator: Any,
    denominator: Any,
    default: Optional[float] = 0.0
) -> Optional[float]:
    """Divide numbers safely while handling zero denominators and bad types."""
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0.0:
            return default
        return num / den
    except (ValueError, TypeError, OverflowError):
        return default
