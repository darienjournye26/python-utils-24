from typing import Any, Dict, Optional, Callable

class DataHandler:
    """Handles data processing pipelines for python-utils-24."""

    def __init__(self, debug: bool = False) -> None:
        self.debug = debug
        self.registry: Dict[str, Callable[[Any], Any]] = {}

    def register_processor(self, name: str, func: Callable[[Any], Any]) -> None:
        """Register a processing function by name."""
        self.registry[name] = func

    def execute(self, name: str, data: Any) -> Optional[Any]:
        """Execute a registered processor with provided data."""
        processor = self.registry.get(name)
        if not processor:
            if self.debug:
                print(f"Warning: Processor '{name}' not found.")
            return None

        try:
            return processor(data)
        except Exception as e:
            if self.debug:
                print(f"Error processing {name}: {e}")
            return None

    def clear_registry(self) -> None:
        """Remove all registered processors."""
        self.registry.clear()