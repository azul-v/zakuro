# Zakuro – Linux package manager

✨️ Just run one command and install your software from archives! 

**Example:**

You have: ``software_v0.0.1-stable_linux.x86_64.tar.gz``

Then: 

```bash
zakuro install ./software_v0.0.1-stable_linux.x86_64.tar.gz
```

**Done!**

## Installation

> [!IMPORTANT]
> *The installation instructions below assume the use of Debian-based Linux distributions; please adapt them for your distribution*

1. Find the ``.bashrc`` file in your home directory, paste the line bellow into it:

```bash
export PATH="$PATH:/home/YOUR_USER_NAME/.zakuro/bin"
```

2. Run:

```bash
sudo apt install pipx
git clone https://github.com/azul-v/zakuro
pipx install ./zakuro
```

## Usage

The ``--help`` flag is your best friend 😉️!

> [!IMPORTANT]
> *This package manager knows nothing about dependencies because package archives are usually self-contained*

## License

This project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
