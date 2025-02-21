from metafind.client import Client

import exiftool


class ExifToolClient(Client):
    """
    ExifToolClient is a wrapper built around the `exiftool.ExifToolHelper` class.
    """

    def __init__(self, path: str):
        self.et = exiftool.ExifToolHelper()
        self.path = path
