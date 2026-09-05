# Copyright (c) 2026 @azul-v
#
# This file is part of Zakuro.
#
# Zakuro is free software: you can redistribute
# it and/or modify it under the terms of the GNU
# General Public License as published by the Free
# Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Zakuro is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU
# General Public License along with Zakuro. If
# not, see <https://www.gnu.org/licenses/>.

import fnmatch
import json
import os
import pathlib
import shutil
import stat
import subprocess

import click
import magic

__version__ = 1

DATABASE = pathlib.Path("/var/lib/zakuro/database.json")
PACKAGES_DIR = pathlib.Path("/opt")
BIN_DIR = pathlib.Path("/usr/bin")
DESKTOP_DIR = pathlib.Path("/usr/share/applications")

runtime_database = dict()


def write_database_changes():
    with open(DATABASE, "w") as file:
        json.dump(runtime_database, file)


@click.group(context_settings={"show_default": True})
@click.version_option(__version__)
def main():
    global runtime_database

    DATABASE.parent.mkdir(parents=True, exist_ok=True)

    if DATABASE.exists():
        with open(DATABASE, "r") as file:
            runtime_database = json.load(file)


@main.command()
@click.option("--exclude", "-e", default="", help="Files to exclude from installation (Unix shell-style wildcard)")
@click.option("--exec-mime-type", "-x", default="application/x-executable", help="Executable MIME type (Unix shell-style wildcard)")
@click.argument("packages", type=click.Path(exists=True, file_okay=False, dir_okay=True), nargs=-1)
def install(exclude, exec_mime_type, packages):
    """Install package(s)"""

    global runtime_database

    for package in packages:
        package = pathlib.Path(package)
        installation_directory = PACKAGES_DIR.joinpath(package.name)
        shutil.copytree(package, installation_directory, dirs_exist_ok=True)

        if not runtime_database.get(package.name):
            runtime_database[package.name] = list()

        for found in installation_directory.rglob("*"):
            relative = found.relative_to(installation_directory)

            if found.is_file() and not fnmatch.fnmatchcase(str(relative), exclude):
                path = None

                if fnmatch.fnmatchcase(magic.from_file(found, mime=True), exec_mime_type):
                    path = BIN_DIR.joinpath(found.name)
                    path.symlink_to(found)
                    os.chmod(path, path.stat().st_mode | stat.S_IEXEC)
                elif found.suffix == ".desktop":
                    path = DESKTOP_DIR.joinpath(found.name)
                    subprocess.Popen(["desktop-file-install", "--dir", DESKTOP_DIR, found])

                if path and str(path) not in runtime_database[package.name]:
                    runtime_database[package.name].append(str(path))


@main.command()
def show():
    """Show installed package(s)"""

    global runtime_database

    for key in runtime_database.keys():
        click.echo(key)


@main.command()
@click.argument("packages", nargs=-1)
def remove(packages):
    """
    Remove package(s)

    Use the package(s) name(s) from the "zakuro show" command
    """

    global runtime_database

    for package in packages:
        for file in runtime_database[package]:
            pathlib.Path(file).unlink()

        package_dir = PACKAGES_DIR.joinpath(package)
        shutil.rmtree(package_dir)
        del runtime_database[package]


if __name__ == "__main__":
    try:
        main()
    finally:
        write_database_changes()
