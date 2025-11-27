"""Tests for API client."""

import unittest

from dotenv import load_dotenv
from src.api.client import APIClient


class TestAPIClient(unittest.TestCase):
    """Test cases for APIClient."""

    def setUp(self):
        load_dotenv()
        
        self.client = APIClient()

    def tearDown(self):
        pass

    def test_get_request(self):
        pass

    def test_post_request(self):
        pass

    def test_error_handling(self):
        pass
