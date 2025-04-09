import json
from scrapli.driver.core import IOSXEDriver

IOSXE_SANDBOX = {
    "host": "devnetsandboxiosxe.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

with IOSXEDriver(**IOSXE_SANDBOX) as conn:
    response = conn.send_command("show version")
    response2 = conn.send_command("sh int desc")

print(response.result)

result_parsed = response.textfsm_parse_output()
print(result_parsed)

result_json = json.dumps(response.textfsm_parse_output(), indent=2)
print(result_json)

result2_json = json.dumps(response2.textfsm_parse_output(), indent=2)
print(result2_json)

loopback10_desc = ['interface Lo10', 'description "Interface Loopback10"']

with IOSXEDriver(**IOSXE_SANDBOX) as conn:
    response2 = conn.send_configs(loopback10_desc)
    response = conn.send_command("sh int desc")

result_json = json.dumps(response.textfsm_parse_output(), indent=2)
print(result_json)
print(response2.result)
