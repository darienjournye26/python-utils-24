import functools
import itertools
from typing import Any, Callable, Iterable, List, Optional


class FastBatchProcessor:
    """Optimized batch processor utilizing slots and iterator slice evaluation."""

    __slots__ = ("batch_size", "_transform")

    def __init__(
        self, batch_size: int = 1000, transform: Optional[Callable[[Any], Any]] = None
    ) -> None:
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")
        self.batch_size = batch_size
        self._transform = transform

    def process_stream(self, iterable: Iterable[Any]) -> Iterable[List[Any]]:
        """Yield batches of processed items without loading full dataset into memory."""
        iterator = iter(iterable)
        transform_fn = self._transform
        
        while True:
            batch = list(itertools.islice(iterator, self.batch_size))
            if not batch:
                break
            if transform_fn is not None:
                yield [transform_fn(item) for item in batch]
            else:
                yield batch


@functools.lru_cache(maxsize=2048)
def memoized_evaluation(key: str, value: Any) -> Any:
    """Fast lookup wrapper for costly repetitive transformation tasks."""
    if isinstance(value, (int, float)):
        return value * 2 - (value % 3)
    return hash((key, str(value)))
