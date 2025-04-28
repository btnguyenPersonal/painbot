#!/bin/bash

REPO_DIR="/home/ben/git/painbot"
SCRIPT_NAME="painbot.py"
BRANCH="main"
CHECK_INTERVAL=60

cd "$REPO_DIR" || exit 1

while true; do
    # Fetch the latest changes from the repository
    git fetch origin "$BRANCH"

    # Check if the local branch is behind the remote branch
    if [ "$(git rev-parse HEAD)" != "$(git rev-parse origin/$BRANCH)" ]; then
        echo "New changes detected. Pulling updates..."
        git pull origin "$BRANCH"

        # Stop the currently running painbot.py (if any)
        pkill -f "python3 $SCRIPT_NAME"

        # Wait briefly to ensure the process has stopped
        sleep 1

        # Start the new version of painbot.py in the background
        nohup python3 "$SCRIPT_NAME" > painbot.log 2>&1 &
        echo "Started new version of $SCRIPT_NAME"
    fi

    # Wait before checking again
    sleep "$CHECK_INTERVAL"
done
