#!/bin/bash

# Install the virtual environment, if successful launch the requirements.txt

#!/bin/bash

# Set the path to the virtual environment
VENV_PATH="./myapp/.venv"

# Install the virtual environment
python3 -m venv "$VENV_PATH"

# Check if venv is created
if [ -d "$VENV_PATH" ]; then
    echo "Virtual environment created successfully."
    # Activate the virtual environment
    source "$VENV_PATH/bin/activate"

    # Now install dependencies from requirements.txt
    chmod +x scripts/init_dependencies.sh
    ./scripts/init_dependencies.sh
else
    echo "Failed to create virtual environment."
    echo "Please try again."
fi
