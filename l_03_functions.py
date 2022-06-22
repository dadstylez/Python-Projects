from random import choice
inport string
from tabulate import tabulate

def create_devices(num_devices=1, num_subnets=1):

    # Create List of Devices
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print("Error: too many devices and/or subnets requested")
        return created_devices

    for subnet_index in range(1, num_subnets+1):

        for device_index in range(1, num_devices+1):

            # Create Device Dictionary
            device = dict()

            # Random Device Name
            device["name"] = (
                choice(["r2", "r3", "r4", "r6", "r18"])
                + choice(["L", "U"])
                + choice(string.ascii_letters)
            )

            # Random Vendor From Choice of Cisco, Juniper, Arista
            device["vendor"] = choice(["cisco", "juniper", "arista"])
            if device["vendor"] == "cisco":
                device["os"] = choice(["ios", "iosxe", "iosxr", "nexus"])
                device["version"] = choice(["12.1(T).84", "14.87X", "8.12(S).010", "20.45"])
            elif device["vendor"] == "juniper":
                device["os"] = choice = "junos"
                device["version"] = choice(["36.23.1", "8.43.12", "6.45", "6.83"])
            elif device["vendor"] == "arista":
                device["os"] = choice = "eos"
                device["version"] = choice(["2.45", "2.55", "2.92.145", "3.01"])
            device["ip"] = "10.1.1." + str(index)

            # Nicely Formatted Print of This One Device

            print()
            for key, value in device.items():
                print(f"{key:>16s} : {value}")

            # Add This Device To The List of Devices
            devices.append(device)
        # Use PPrint to Print Data As-Is
        print("\n----- Devices As List of Dicts --------------")
        pprint(devices)

        # Use Tabulate to print Table of Devices
        print("\n----- sorted Devices in Tabular Format -----------")
        print(tabulate(sorted(devices, key=itemgetter("vendor", "os", "version")), headers="keys"))


