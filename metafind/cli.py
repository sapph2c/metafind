from metafind.logging import log
from metafind.client import Client
from metafind.clientfactory import get_client
from metafind.errors import MetafindError
from metafind.output import fetch_output

from rich.console import Console

import click
import sys


@click.group()
def cli():
    pass


def common_options(func):
    """
    Decorator to attach the same CLI options ('path', 'backend')
    to each command.
    """
    func = click.argument("path", required=True)(func)
    func = click.option(
        "--backend",
        help="Specify a metadata analyzer backend",
        default="exiftool",
        required=True,
    )(func)
    return func


def handle_command(func):
    """
    Decorator to create the backend client and CLI console, as well as handle any exceptions.
    """

    def wrapper(path, backend, *args, **kwargs):
        try:
            client = get_client(backend, path)
            console = Console()
            return func(client, console, *args, **kwargs)
        except MetafindError as e:
            log.error(e)
            sys.exit(e.error_code)

    # Preserve function metadata (so click doesn't get confused)
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


@cli.command()
@common_options
@handle_command
def fetch(client: Client, console: Console) -> None:
    """
    Retrieves a list of all metadata found within the file(s) at the specified path.
    """
    result = client.get_metadata()
    console.print(fetch_output(result))


@cli.command()
@common_options
@handle_command
def scrub(client: Client, console: Console):
    """
    Attempts to scrub all metadata found within the file(s) at the specified path.
    """
    pass


@cli.command()
@common_options
@handle_command
def unique(client: Client, console: Console) -> None:
    """
    Gets an alphabetized list of all unique metadata tags found within the file(s) at the specified path.
    """
    result = client.get_unique_tags()
    console.print(result)
