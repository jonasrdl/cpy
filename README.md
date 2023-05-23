# cpy

This Python script automates the process of checking for updates and installing the latest version of the Discord Canary package on a Linux system.

### The script performs the following steps:

- Retrieves the current installed version of Discord Canary using the apt package manager.
- Downloads the latest version of Discord Canary from the official download URL.
- Compares the versions to determine if an update is available.
- If an update is available, the new package is installed using dpkg.
- The downloaded package is deleted after installation or if no update is available.
- This script allows Discord Canary users to automate the update process, ensuring they always have the latest version without manual intervention.
