"""Main application entry point."""

import api.client


class Application:
    """Main application class."""

    def __init__(self):
        pass

    def run(self):
        """Run the application."""
        pass

    def setup(self):
        """Initialize application components."""
        pass

    def cleanup(self):
        """Clean up resources."""
        pass


def main():
    response = api.client.APIClient().get("user")
    print(response.json())
    """Application entry point."""
    pass


if __name__ == "__main__":
    main()