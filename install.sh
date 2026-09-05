#!/bin/sh

pyinstaller -F -n zakuro main.py
sudo cp dist/zakuro /usr/local/bin
