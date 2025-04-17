import httpx
from rich import print as rprint

IOSXE_SANDBOX = {
    "host": "https://devnetsandboxiosxe.cisco.com:443/restconf/data/native/router/bgp",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

headers = {'Accept': 'application/yang-data+json',
           'Content-Type': 'application/yang-data+json',
           }

def pull_info():
    with httpx.Client(verify=False) as client:
        response = client.get(IOSXE_SANDBOX["host"], headers=headers,
                              auth=(IOSXE_SANDBOX["auth_username"], IOSXE_SANDBOX["auth_password"]))
        return response.text

results = pull_info()
rprint(results)
