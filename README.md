# Zakuro – The Linux package manager

The Linux package manager that installs packages from any archives!

## The story

Many programs are distributed using AppImage, portable archives, or single binary files. But where should you install all of this? It's usually a boring routine.

But with this tool, you don't need to worry about that. Just download your package archive and run one command!

> [!IMPORTANT]
> *This package manager knows nothing about dependencies because package archives are usually self-contained*

## Installation

> [!IMPORTANT]
> *The installation instructions below assume the use of Debian-based Linux distributions; please adapt them for your distribution*

1. Add ``/home/YOUR_USER_NAME/.zakuro/bin`` to your PATH:

```bash
export PATH="$PATH:/home/YOUR_USER_NAME/.zakuro/bin"
```

2. Install pipx:

```bash
sudo apt install pipx
```

3. Clone the repository:
```bash
git clone https://github.com/azul-v/zakuro
```

4. Install Zakuro:

```bash
pipx install ./zakuro
```

## Usage

The ``--help`` flag is your best friend 😉️!

## License

This project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
