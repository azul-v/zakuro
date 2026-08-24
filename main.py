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

import os
import pathlib
import shutil

import click
import patoolib

__version__ = 1

HOME = pathlib.Path().home()
BIN_PATTERN = "bin/*"

base_dir = HOME.joinpath(".zakuro")
installed_dir = base_dir.joinpath("installed")
bin_dir = base_dir.joinpath("bin")


@click.group()
@click.version_option(__version__)
@click.option("--verbose", is_flag=True)
def main(verbose: bool) -> None:
    base_dir.mkdir(parents=True, exist_ok=True)
    installed_dir.mkdir(exist_ok=True)
    bin_dir.mkdir(exist_ok=True)

    if str(bin_dir) not in os.getenv("PATH"):
        print(f"✋️ Please add {bin_dir} to PATH")
        return


@main.command()
@click.argument(
    "archives",
    type=click.Path(exists=True, file_okay=True, dir_okay=False),
    nargs=-1
)
def install(archives: list[click.Path]) -> None:
    """
    Install packages

    Specify the paths to the packages archives

    All files in the 'bin' directory of the package
    archives will be available globally
    """

    for archive in archives:
        installation_directory = installed_dir.joinpath(
            pathlib.Path(archive).name
        )
        patoolib.extract_archive(str(archive), 2, str(installation_directory))

        for found in installation_directory.rglob(BIN_PATTERN):
            symbolic_link = bin_dir.joinpath(found.name)
            symbolic_link.symlink_to(found)

    print("✨️🎉️✨️ All packages installed successfully!")


@main.command()
def show() -> None:
    """Show installed packages"""

    try:
        next(installed_dir.iterdir())
    except StopIteration:
        print("You haven't installed any packages yet 🤔️")
        return

    print("Installed packages")

    for item in installed_dir.iterdir():
        print(f"└─{item.name}")


@main.command()
@click.argument("packages", nargs=-1)
def remove(packages: list[str]) -> None:
    """
    Remove packages

    Specify the packages names from the output of the 'show' command
    """

    with click.progressbar(
        packages,
        label="Removing packages",
        empty_char=" ",
        fill_char=":"
    ) as progress:
        for package in progress:
            package_dir = installed_dir.joinpath(package)
            shutil.rmtree(package_dir)

            for file in bin_dir.iterdir():
                if file.is_symlink() and file.readlink().is_relative_to(
                    package_dir
                ):
                    file.unlink()


if __name__ == "__main__":
    main()
