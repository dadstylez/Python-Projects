from pprint import pprint

#Disctionary representing a device

device = {
    "name": "sbx-n9kv-ao",
    "vendor": "Nexus9000 C9300v Chassis",
    "os": "nxos",
    "version": "9.3(3)",
    "ip": "10.1.1.1",
}

#Simple Print
print(device)

#Pretty Print
print()
pprint(device)

# For Loop, Nicely Formatted Print
print()
for key, value in device.items():
    print(f"{key:>16s} : {value}")