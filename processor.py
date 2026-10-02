import json
from typing import Any, Dict, List, Optional, Union


class ProcessingError(Exception):
    """Custom exception raised when data transformation fails."""
    pass


def safe_get_nested(data: Any, keys: List[Union[str, int]], default: Optional[Any] = None) -> Any:
    """Safely extract nested dictionary or list items handling index and key errors."""
    if not isinstance(keys, (list, tuple)):
        raise TypeError("Keys argument must be a list or tuple of keys/indices")

    current = data
    for key in keys:
        if current is None:
            return default
        if isinstance(current, dict) and isinstance(key, str):
            current = current.get(key, default)
        elif isinstance(current, (list, tuple)) and isinstance(key, int):
            try:
                current = current[key]
            except IndexError:
                return default
        else:
            return default
    return current


def parse_and_coerce(
    data_str: str,
    target_type: type = dict,
    fallback: Optional[Any] = None
) -> Any:
    """Parse JSON string with fallback handling for malformed input and unexpected types."""
    if not isinstance(data_str, str):
        if fallback is not None:
            return fallback
        raise TypeError(f"Expected str input, got {type(data_str).__name__}")

    stripped = data_str.strip()
    if not stripped:
        return fallback

    try:
        parsed = json.loads(stripped)
    except (json.JSONDecodeError, TypeError, ValueError):
        return fallback

    if target_type and not isinstance(parsed, target_type):
        return fallback

    return parsed


def safe_divide_metrics(numerator: Any, denominator: Any, precision: int = 4) -> float:
    """Calculate division while safely handling zero division and non-numeric inputs."""
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0.0 or num != num or den != den:
            return 0.0
        result = num / den
        if result == float('inf') or result == float('-inf'):
            return 0.0
        return round(result, precision)
    except (ValueError, TypeError):
        return 0.0
