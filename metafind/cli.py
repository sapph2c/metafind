from metafind.logging import log


import rich
import click


@click.command()
@click.argument("path", required=True)
def cli(path: str):
    try:
        pass
    except Exception as e:
        log.error(e)
