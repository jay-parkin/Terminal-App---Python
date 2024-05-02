#1/bin/bash

# initialise all the required dependencies
# beautifulsoup4==4.12.3
# certifi==2024.2.2
# charset-normalizer==3.3.2
# idna==3.7
# markdown-it-py==3.0.0
# mdurl==0.1.2
# Pygments==2.17.2
# pyreadline3==3.4.1
# requests==2.31.0
# rich==13.7.1
# soupsieve==2.5
# urllib3==2.2.1

#!/bin/bash

# Run pip install
pip install -r requirements.txt

# Check the exit status
if [ $? -eq 0 ]; then
    echo "Installation successful"

    # Starting app
    chmod +x scripts/start_app.sh
    ./scripts/start_app.sh
else
    echo "Failed to install requirements."
    echo "Please and try again."
fi
