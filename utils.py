import time
import random
from functools import wraps

def retry_on_failure(max_retries: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """Apply retry logic with exponential backoff and jitter.
    Intended for transient network operation failures.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            last_exc = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exc = exc
                    if attempt == max_retries - 1:
                        raise last_exc
                    # jitter to prevent synchronized retries
                    jittered_delay = current_delay * random.uniform(0.8, 1.2)
                    time.sleep(jittered_delay)
                    current_delay = min(current_delay * backoff, 30.0)  # cap delay
            raise RuntimeError("Retry logic failed unexpectedly")
        return wrapper
    return decorator

class NetworkOperationSimulator:
    """Simulates network ops for testing retry logic."""
    def __init__(self):
        self.call_count = 0
    def perform_operation(self, payload):
        self.call_count += 1
        if self.call_count < 3:
            # Simulate transient network issues
            raise ConnectionError("Temporary network failure")
        return f"Operation successful with payload: {payload}"

# Create simulator instance
sim = NetworkOperationSimulator()

@retry_on_failure(max_retries=4, delay=0.05, backoff=1.5)
def execute_network_op(data):
    """Wrapper for the simulated network call."""
    return sim.perform_operation(data)

# Demonstration that it works
if __name__ == "__main__":
    try:
        result = execute_network_op("sample request")
        print(result)
        print(f"Total calls made: {sim.call_count}")
    except Exception as e:
        print(f"Error: {e}")
