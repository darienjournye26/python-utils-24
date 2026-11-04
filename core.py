import functools
import itertools
from typing import Any, Callable, Iterable, List, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class CoreBatchProcessor:
    """High-performance batch processing utility with memory-conscious iteration."""

    def __init__(self, batch_size: int = 1000):
        if batch_size <= 0:
            raise ValueError("Batch size must be a positive integer.")
        self.batch_size = batch_size

    def chunk_iterable(self, iterable: Iterable[T]) -> Iterable[List[T]]:
        """Efficiently split an iterable into chunks using itertools islice."""
        iterator = iter(iterable)
        while chunk := list(itertools.islice(iterator, self.batch_size)):
            yield chunk

    @staticmethod
    @functools.lru_cache(maxsize=1024)
    def cached_transform(transform_func: Callable[[Any], Any], value: Any) -> Any:
        """Apply pure transformation with LRU cache to eliminate duplicate work."""
        return transform_func(value)

    def process_fast(self, items: List[T], transform: Callable[[T], R]) -> List[R]:
        """Process items with local method reference binding for optimized loop speed."""
        results: List[R] = []
        append = results.append
        for item in items:
            append(transform(item))
        return results

    def map_in_chunks(self, items: Iterable[T], transform: Callable[[T], R]) -> List[R]:
        """Process large iterables in chunks to maintain low memory overhead."""
        output: List[R] = []
        extend = output.extend
        for chunk in self.chunk_iterable(items):
            processed = self.process_fast(chunk, transform)
            extend(processed)
        return output
