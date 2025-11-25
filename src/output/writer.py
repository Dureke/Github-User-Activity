"""Output writer for different destinations."""


class OutputWriter:
    """Writes formatted data to various outputs."""

    def __init__(self):
        pass

    def write_to_file(self, data, filepath: str):
        """Write data to file."""
        pass

    def write_to_console(self, data):
        """Write data to console."""
        pass

    def write_to_stream(self, data, stream):
        """Write data to stream."""
        pass
