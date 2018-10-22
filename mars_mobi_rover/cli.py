# -*- coding: utf-8 -*-

"""Console script for mars_mobi_rover."""
import sys

import click


@click.command()
def main(args=None):
    """Console script for mars_mobi_rover."""
    stdin_text = click.get_text_stream('stdin').read()
    if stdin_text:
        click.echo(stdin_text)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
