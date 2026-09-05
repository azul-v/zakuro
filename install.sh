#!/bin/sh

pyinstaller -F -n zakuro main.py
chmod +x dist/zakuro
sudo mv dist/zakuro /usr/local/bin/zakuro
