from metafind.client import Client
from metafind.exiftool import ExifToolClient
from metafind.errors import UnsupportedBackend


def get_client(backend: str, path: str) -> Client:
    match backend:
        case "exiftool":
            return ExifToolClient(path)
        case _:
            raise UnsupportedBackend(backend)
