#!/bin/bash

# Define the desired Python version
desired_version="3.10.12"

# Get the installed Python version
installed_version=$(python3 --version 2>&1)

# Extract the version number from the output
installed_version=${installed_version:7}

# Compare the installed version with the desired version
if [[ "$installed_version" == "$desired_version" ]]; then
    echo "Python version $desired_version is installed."
else
    echo "Python version $desired_version is not installed."
fi
