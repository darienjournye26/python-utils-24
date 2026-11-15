from typing import Any, Iterable, Optional, Dict

def chunk_list(data: Iterable[Any], size: int) -> Iterable[list[Any]]:
    """Split an iterable into chunks of a specified size."""
    if size <= 0:
        raise ValueError("Chunk size must be a positive integer.")
    
    chunk = []
    for item in data:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk

def merge_dicts(*dicts: Dict[Any, Any]) -> Dict[Any, Any]:
    """Merge multiple dictionaries into a single result dictionary."""
    result: Dict[Any, Any] = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

def format_string(template: str, context: Optional[Dict[str, Any]] = None) -> str:
    """Safe string formatting using a provided context dictionary."""
    if not context:
        return template
    return template.format(**context)

def get_nested(data: Dict[Any, Any], keys: Iterable[Any], default: Any = None) -> Any:
    """Retrieve a value from a nested dictionary structure."""
    current = data
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current