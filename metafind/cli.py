from metafind.logging import log
from metafind.helper import get_client


import rich
import click


@click.command()
@click.argument("path", required=True)
@click.option(
    "--backend",
    help="specify a specific Metadata backend",
    default="exiftool",
    required=True,
)
def cli(path: str, backend):
    try:
        client = get_client(backend, path)
    except Exception as e:
        log.error(e)
