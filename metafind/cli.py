from metafind.logging import log
from metafind.helper import get_client
from metafind.errors import MetafindError
from metafind.output import fetch_output

from rich.console import Console
from rich import print

import click


@click.group()
def cli():
    pass


@cli.command()
@click.argument("path", required=True)
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
        console = Console()
        client = get_client(backend, path)
        result = client.get_metadata()
        console.print(fetch_output(result))
    except MetafindError as e:
        log.error(e)
        exit(e.error_code)


@cli.command()
@click.argument("path", required=True)
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


@cli.command()
@click.argument("path", required=True)
@click.option(
    "--backend",
    help="specify a Metadata analyzer backend",
    default="exiftool",
    required=True,
)
def unique(path: str, backend):
    """
    Gets an alphabetized list of all unique metadata tags found within the file(s) at the specified path.
    """
    try:
        client = get_client(backend, path)
        result = client.get_unique()
        print(result)
    except MetafindError as e:
        log.error(e)
        exit(e.error_code)
