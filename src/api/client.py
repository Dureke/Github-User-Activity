"""API client for handling HTTP requests."""


import os
from dotenv import load_dotenv
import requests


class APIClient:
    """Handles API requests and responses."""

    def __init__(self):
        load_dotenv()

        self.base_url = os.getenv("API_BASE_URL")
        self.api_key = os.getenv("API_KEY")
        pass

    def get(self, endpoint: str, params: dict = None):
        """Send GET request to API endpoint."""
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", params=params, headers={"Authorization": f"token {self.api_key}"})
            return response
        except requests.RequestException as e:
            self._handle_error(e)

    def post(self, endpoint: str, data: dict = None):
        """Send POST request to API endpoint."""
        try:
            response = requests.post(f"{self.base_url}/{endpoint}", json=data, headers={"Authorization": f"token {self.api_key}"})
            return response
        except requests.RequestException as e:
            self._handle_error(e)

    def _handle_response(self, response):
        """Process API response."""
        pass

    def _handle_error(self, error):
        """Handle API errors."""
        print(f"API request error: {error}")
        pass
