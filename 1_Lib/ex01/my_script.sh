#!/bin/bash

echo "Using pip version:"
pip --version

# Define installation directory relative to this script
INSTALL_DIR="$(dirname "$0")/local_lib"

# Create the directory if it doesn't exist
mkdir -p "$INSTALL_DIR"

# Install path.py from GitHub repository, crush existing installation
pip install --target="$INSTALL_DIR" --log path_install.log --upgrade --force-reinstall git+https://github.com/jaraco/path.git

# Check if path.py was installed correctly by verifying if path is in the installed packages
if python -c "import sys; sys.path.append('$INSTALL_DIR'); import path" &> /dev/null; then
  echo "path.py installed successfully."
  # Run the Python program
  python "$(dirname "$0")/my_program.py"
else
  echo "Failed to install path.py."
fi

