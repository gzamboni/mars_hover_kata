# -*- coding: utf-8 -*-

"""Console script for mars_mobi_rover."""
import sys

import click

from mars_mobi_rover.mission import Mission


@click.command()
def main(args=None):
    """Console script for mars_mobi_rover."""
    stdin_text = click.get_text_stream('stdin').read()
    if stdin_text:
        mission = Mission(stdin_text)
        result = mission.execute()
        click.echo(result)
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
