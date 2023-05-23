import requests
import re
import os
import subprocess

download_url = "https://discord.com/api/download/canary?platform=linux&format=deb"

package_name = "discord-canary"
apt_command = f"apt show {package_name}"
result = subprocess.run(apt_command, shell=True, capture_output=True, text=True)

version_pattern = r"Version: (\d+\.\d+\.\d+)"
match = re.search(version_pattern, result.stdout)
if match:
    current_version = match.group(1)
    print(f"Current version: {current_version}")
else:
    print("Unable to retrieve the current version.")
    exit(1)

response = requests.get(download_url)

filename = response.url.split("/")[-1]
version_pattern = r"discord-canary-(\d+\.\d+\.\d+)\.deb"
match = re.search(version_pattern, filename)
if match:
    new_version = match.group(1)
    print(f"New version: {new_version}")
else:
    print("Unable to extract the new version from the filename.")
    exit(1)

if new_version > current_version:
    print("There is an update available, updating...")

    with open(filename, "wb") as file:
        file.write(response.content)

    install_command = f"sudo dpkg -i {filename}"
    subprocess.run(install_command, shell=True)

    print(f"Updated to version {new_version}. Package installed.")

    os.remove(filename)
    print("Downloaded file deleted.")
else:
    os.remove(filename)
    print("No update available. Downloaded file deleted.")
