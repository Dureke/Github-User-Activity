"""Main application entry point."""

import api.client as APIClient


class Application:
    """Main application class."""

    def __init__(self):
        self.client = APIClient.APIClient()
        self.setup()

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
    app = Application()
    response = app.client.get("user")
    print(response)
    """Application entry point."""
    pass


if __name__ == "__main__":
    main()