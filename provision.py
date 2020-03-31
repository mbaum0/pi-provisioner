from subprocess import check_output
import os

# get list of drives (windows DOS)
output = check_output("wmic logicaldisk get caption", shell=True).decode()

# remove CR, colons, and spaces
output = output.replace(' ', '').replace('\r','').replace(':','')

# make list of drives by newlines, remove first entry (text from cmd)
output = output.split('\n')[1:]

# sometimes empty entries show up if drive is not mounted (I think)
# this removes any empty entries
drives = list(filter(None, output))


# setup a drive picker

selected_drive = None

while selected_drive not in drives:
    
    print('Available drives are: ', end=' ')
    
    for i in range(len(drives)):
        if i < len(drives) -1:
            print(drives[i], end=', ')
        else:
            print(drives[i])

    selected_drive = input('Enter the boot partition drive: ').upper()

    if (selected_drive in drives):
        break

    print('Invalid drive!')


print('Selected drive: ', selected_drive)

net_ssid = input('Enter WiFi SSID: ').strip()
net_pass = input('Enter WiFi Password: ').strip()

print(' - Creating ssh file')
with open(os.path.join(selected_drive+':', 'ssh'), 'wb'):
    pass

print(' - Creating wpa_supplicant file')
with open(os.path.join(selected_drive+':', 'wpa_supplicant.conf'), 'w') as wpas_file:
    wpas_file.write("ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n")
    wpas_file.write("update_config=1\n")
    wpas_file.write("country=US\n")
    wpas_file.write("network={\n")
    wpas_file.write("  ssid=\"%s\"\n" % net_ssid)
    wpas_file.write("  psk=\"%s\"\n" % net_pass)
    wpas_file.write("}\n")

print(" - Done!")

print("Your Raspbian SD card has been provisioned. You can now eject the drive.")