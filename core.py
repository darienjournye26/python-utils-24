import functools
import itertools
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Callable, Iterable, List, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class FastPipeline:
    """High-performance batch execution and memoized pipeline helper."""

    def __init__(self, max_workers: int = 4, cache_size: int = 128) -> None:
        self.max_workers = max_workers
        self.cache_size = cache_size

    def chunk_iterable(self, iterable: Iterable[T], chunk_size: int) -> Iterable[List[T]]:
        """Split an iterable into chunks of fixed size without excess memory usage."""
        iterator = iter(iterable)
        while chunk := list(itertools.islice(iterator, chunk_size)):
            yield chunk

    def memoize(self, func: Callable[..., R]) -> Callable[..., R]:
        """Wrap a callable with an LRU cache for result reuse."""
        return functools.lru_cache(maxsize=self.cache_size)(func)

    def map_parallel(self, func: Callable[[T], R], items: Sequence[T], chunk_size: int = 100) -> List[R]:
        """Execute mapping in parallel over items using worker pool and chunking."""
        if not items:
            return []

        results: List[R] = []
        chunks = list(self.chunk_iterable(items, chunk_size))

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [
                executor.submit(lambda c: [func(item) for item in c], chunk)
                for chunk in chunks
            ]
            for future in futures:
                results.extend(future.result())

        return results
