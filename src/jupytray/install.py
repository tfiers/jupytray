"""
Commands to add & remove a shortcut to the Windows Start Menu that starts Jupytray.
"""

import click


@click.group()
def cli():
    pass


@cli.command()
def install():
    """ Add a shortcut to the Windows Start menu to run Jupytray. """
    ...


@cli.command()
def uninstall():
    """ Remove the shortcuts installed by `jupytray install`. """
    ...
