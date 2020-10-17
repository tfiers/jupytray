import sys
from pathlib import Path

import click
import winshell

from .icon import icon_path


@click.group()
def cli():
    pass


@cli.command()
def install():
    """ Add a shortcut to the Windows Start menu to run Jupytray. """
    create_shortcut(start_menu_dir)
    create_shortcut(startup_dir)


@cli.command()
def uninstall():
    """ Remove the shortcuts installed by `jupytray-shortcuts install`. """
    remove_shortcut(start_menu_dir)
    remove_shortcut(startup_dir)


start_menu_dir = Path(winshell.folder("startmenu")) / "Programs"
startup_dir = Path(winshell.folder("startup"))
conda_root = Path(sys.base_prefix)


def get_shortcut_path(dir: Path):
    return dir / "Jupytray.lnk"


def create_shortcut(dir):
    shortcut_path = get_shortcut_path(dir)
    with winshell.shortcut(str(shortcut_path)) as shortcut:
        shortcut.path = str(conda_root / "pythonw.exe")
        shortcut.arguments = "-m jupytray"
        shortcut.working_directory = str(conda_root)
        shortcut.icon_location = (str(icon_path), 0)
    click.echo(f"Created shortcut <{shortcut_path}>")


def remove_shortcut(dir):
    shortcut_path = get_shortcut_path(dir)
    shortcut_path.unlink(missing_ok=True)
    click.echo(f"Removed shortcut <{shortcut_path}>")
