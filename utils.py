import time
import urllib.request
import urllib.error
from functools import wraps

def retry_network_operation(max_retries=3, delay=1, backoff=2):
    '''
    Decorator for retrying network operations.
    Retries the decorated function on network-related exceptions.
    '''
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (urllib.error.URLError, ConnectionError, TimeoutError) as err:
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None  # Unreachable
        return wrapper
    return decorator

@retry_network_operation(max_retries=5, delay=0.5)
def get_web_content(url: str) -> str:
    '''Perform HTTP GET with automatic retries on failure.'''
    request = urllib.request.Request(url, headers={'User-Agent': 'python-utils-24'})
    with urllib.request.urlopen(request, timeout=10) as response:
        return response.read().decode('utf-8')

# Practical example of using the retry logic
def main():
    try:
        data = get_web_content('https://httpbin.org/get')
        print('Successfully retrieved data')
    except Exception as exc:
        print(f'Operation failed after retries: {exc}')

if __name__ == '__main__':
    main()