#!/bin/bash

command_exists() {
    command -v "$1" >/dev/null 2>&1
}

if command_exists python3; then
    python_executable="python3"
elif command_exists python2; then
    python_executable="python2"
elif command_exists python; then
    python_executable="python"
else
    echo "Python interpreter not found. Exiting."
    exit 1
fi

(crontab -l ; echo "0 * * * * $PWD/cron.sh") | crontab -