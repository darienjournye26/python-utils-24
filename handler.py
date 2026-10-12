from typing import Any, Callable, Dict, Optional
import logging

logger = logging.getLogger(__name__)

class RequestHandler:
    """Handles incoming requests with optional pre-processing."""

    def __init__(self, middleware: Optional[Callable[[Dict[str, Any]], Dict[str, Any]]] = None) -> None:
        """Initialize handler with an optional transformation middleware."""
        self.middleware = middleware

    def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Processes the payload and returns the transformed result."""
        try:
            if self.middleware:
                payload = self.middleware(payload)
            
            return {"status": "success", "data": payload}
        except Exception as e:
            logger.error(f"execution failed: {e}")
            return {"status": "error", "message": str(e)}

def validate_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    """Ensures that the required keys are present."""
    if "id" not in data:
        raise ValueError("missing required field: id")
    return data

if __name__ == "__main__":
    handler = RequestHandler(middleware=validate_payload)
    result = handler.execute({"id": 1, "value": "test"})
    print(result)