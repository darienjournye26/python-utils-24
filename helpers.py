from typing import Any, Iterable, Dict, Optional

def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '_') -> Dict[str, Any]:
    """
    Flatten a nested dictionary structure using a separator.
    Useful for converting complex JSON or configs into flat structures.
    """
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def chunk_iterable(data: Iterable[Any], size: int) -> Iterable[Any]:
    """
    Yield successive chunks from an iterable for batch processing.
    """
    it = iter(data)
    while True:
        chunk = []
        try:
            for _ in range(size):
                chunk.append(next(it))
            yield chunk
        except StopIteration:
            if chunk:
                yield chunk
            break

def get_nested(data: Dict[str, Any], path: str, default: Any = None) -> Any:
    """
    Access nested dictionary values using dot notation keys.
    Example: get_nested(config, 'db.port', 5432)
    """
    keys = path.split('.')
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data