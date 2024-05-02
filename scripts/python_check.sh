#!/bin/bash

# check whether the user's installed version of python
# is the same or higher.

# Desired Python version
desired_version="3.10.12"

# Get the installed Python version
installed_version=$(python3 --version 2>&1 | awk '{print $2}')

# Use sort to compare versions. 
# Add the desired version and the installed version to a list
# sort them and check if the installed version comes first.
higher_version=$(echo -e "$desired_version\n$installed_version" | sort -V | head -n 1)

# Compare the sorted first version with the desired version
if [[ "$higher_version" == "$desired_version" ]]; then
    echo "Current Python installed satisfies the required version: $desired_version."
    echo "Proceeding to install required dependencies..."

    chmod +x scripts/init_venv.sh
    ./scripts/init_venv.sh

else
    echo "Current installed Python-$installed_version does not meet required version: $desired_version."
    echo "Please update Python and try again."
fi