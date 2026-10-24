import functools
import itertools
from typing import Any, Callable, Iterable, List, Sequence, TypeVar

T = TypeVar("T")
R = TypeVar("R")


class BatchProcessor:
    """Optimized batch processor using stream chunking and transformation caching."""

    def __init__(self, batch_size: int = 1000):
        if batch_size <= 0:
            raise ValueError("batch_size must be a positive integer")
        self.batch_size = batch_size

    def chunk_iterable(self, iterable: Iterable[T]) -> Iterable[List[T]]:
        """Yield successive chunks from iterable without memory overhead."""
        iterator = iter(iterable)
        while True:
            chunk = list(itertools.islice(iterator, self.batch_size))
            if not chunk:
                break
            yield chunk

    @staticmethod
    @functools.lru_cache(maxsize=2048)
    def _memoized_transform(func: Callable[[Any], Any], item: Any) -> Any:
        """Memoize pure function transformations on individual elements."""
        return func(item)

    def process_stream(
        self, data: Iterable[T], transform: Callable[[T], R], use_cache: bool = False
    ) -> Iterable[R]:
        """Process stream in optimized chunks to minimize memory consumption."""
        for chunk in self.chunk_iterable(data):
            if use_cache:
                yield from (self._memoized_transform(transform, item) for item in chunk)
            else:
                yield from (transform(item) for item in chunk)


def fast_flatten(sequences: Sequence[Iterable[T]]) -> List[T]:
    """Perform efficient flattening of nested iterables using itertools chain."""
    return list(itertools.chain.from_iterable(sequences))
