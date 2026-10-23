from typing import Final, Dict, Any

# Configuration settings for system components
DEFAULT_TIMEOUT: Final[float] = 30.0
MAX_RETRIES: Final[int] = 3

# Status codes for internal processing
STATUS_SUCCESS: Final[str] = 'success'
STATUS_FAILURE: Final[str] = 'failure'

# Default application schema mappings
DEFAULT_SETTINGS: Final[Dict[str, Any]] = {
    'debug': False,
    'environment': 'production',
    'version': '1.0.0'
}

def get_app_settings() -> Dict[str, Any]:
    """
    Retrieve the default application configuration dictionary.

    Returns:
        Dict[str, Any]: A copy of the default application settings.
    """
    return DEFAULT_SETTINGS.copy()

class AppConstants:
    """
    Container class for centralized application constants.
    """
    API_VERSION: Final[str] = 'v1'
    HEADER_KEY: Final[str] = 'X-App-ID'

    @staticmethod
    def get_version_info() -> str:
        """
        Return the current API version identifier.

        Returns:
            str: The API version string.
        """
        return AppConstants.API_VERSION