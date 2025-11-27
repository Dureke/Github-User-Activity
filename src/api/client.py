"""API client for handling HTTP requests."""


import os
from dotenv import load_dotenv
import requests


class APIClient:
    """Handles API requests and responses."""

    def __init__(self):
        pass

    def get(self, endpoint: str, params: dict = None):
        load_dotenv()

        base_url = os.getenv("API_BASE_URL")
        api_key = os.getenv("API_KEY")

        response = requests.get(f"{base_url}/user", params=params, headers={"Authorization": f"token {api_key}"})
        return response

    def post(self, endpoint: str, data: dict = None):
        """Send POST request to API endpoint."""
        pass

    def _handle_response(self, response):
        """Process API response."""
        pass

    def _handle_error(self, error):
        """Handle API errors."""
        pass
