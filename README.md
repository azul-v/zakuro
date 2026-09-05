<p align="center"><img src="logo.png" alt="Logo"></p>

<h1 align="center">Zakuro</h1>

<p align="center">Package manager for portable pacakges</p>

## Features

- Easy to use
- Installs portable programs from directories
- Does not require special package configuration

## Installation

Download [the latest release](https://github.com/azul-v/zakuro/releases/latest/download/zakuro) and run:

```bash
chmod +x zakuro
sudo mv zakuro /usr/local/bin/zakuro
```

## Installation from source code

1. Install <a href="https://pipx.pypa.io/latest/how-to/install-pipx.html" target="_blank">pipx</a> and <a href="https://docs.astral.sh/uv/getting-started/installation/" target="_blank">uv</a>
2. Download [the repository](https://github.com/azul-v/zakuro/archive/refs/heads/master.zip)
3. Go to the repository directory
4. Synchronize:

```bash
uv sync
```

5. Activate the environement:

```bash
source .venv/bin/activate
```

6. Run:

```bash
./install.sh
```

## Usage

Use with root privileges and explore with the ``--help`` option 😉️

```bash
sudo zakuro --help
```

## Copyright and license

Copyright (c) 2026 @azul-v

This project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
