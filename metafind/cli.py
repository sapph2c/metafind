from metafind.logging import log
from metafind.helper import get_client
from metafind.errors import MetafindError


import rich
import click


@click.group()
def cli():
    pass


@cli.command()
@click.option("--path", help="path of file(s) to analyze", required=True)
@click.option(
    "--backend",
    help="specify a Metadata analyzer backend",
    default="exiftool",
    required=True,
)
def fetch(path: str, backend):
    """
    Retrieves a list of all metadata found within the file(s) at the specified path.
    """
    try:
        client = get_client(backend, path)
    except MetafindError as e:
        log.error(e)
        exit(e.error_code)


@cli.command()
@click.option("--path", help="path of file(s) to analyze", required=True)
@click.option(
    "--backend",
    help="specify a Metadata analyzer backend",
    default="exiftool",
    required=True,
)
def scrub(path: str, backend):
    """
    Attempts to scrub all metadata found within the file(s) at the specified path.
    """
    try:
        client = get_client(backend, path)
    except MetafindError as e:
        log.error(e)
        exit(e.error_code)
