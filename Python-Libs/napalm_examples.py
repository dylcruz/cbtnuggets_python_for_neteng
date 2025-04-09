from rich import print as rprint
from napalm import get_network_driver

DEVICES = [
    {
        "hostname": "devnetsandboxiosxe.cisco.com",
        "username": "admin",
        "password": "C1sco12345",
        "driver": "ios",
    }
]

for dev in DEVICES:
    driver = get_network_driver(dev['driver'])
    with driver(username=dev['username'], password=dev['password'], hostname=dev['hostname']) as device:
        result = device.get_facts()
    rprint(f'{result["hostname"]} is a {result["vendor"]} device - serial number {result["serial_number"]}')
