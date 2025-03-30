#!/bin/bash

cd /home/backend || exit 1

# Remove old venv if it exists
rm -rf venv

# Create a new virtual environment inside the container
python3 -m venv venv
. venv/bin/activate

pip install -r requirements.txt > /dev/null 2>&1 || { echo "pip install failed"; exit 1; }
