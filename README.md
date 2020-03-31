# pi-provisioner

## About
Provisioning script for raspberry pi. Use to setup a raspberry pi that will be used in a headless environment. This script creates a wpa_supplicant and ssh files in the boot parition of an SD card imaged with raspbian. After running this script, the SD card may be inserted into the raspberry pi and it will auto-connect to wifi and support SSH

## Usage

This script currently only supports windows. In the future I plan to detect OS and find drive letters in linux. The following describes how to use the script

1. Image raspian onto an SD card
2. Determine which drive letter is mapped to the boot parition. This can be done in windows explorer
3. Clone this repo ```git clone https://github.com/mbaum0193/pi-provisioner```
4. cd into main directory ```cd pi-provisioner```
5. Run the script ```python provision.py```
6. Enter boot partition drive letter
7. Enter wifi SSID and Password
8. Eject SD card, place into PI and boot!
