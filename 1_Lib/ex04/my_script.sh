#!/bin/bash

PYTHON_PATH="/usr/bin/python3"
VENE_DIR="django_venv"

# setup venv
python3 -m venv django_venv
source django_venv/bin/activate

# pip version
python -m pip --version

# pip install
python -m pip install --force-reinstall -r requirement.txt
