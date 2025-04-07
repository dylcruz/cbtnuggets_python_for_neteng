from scrapli.driver.core import IOSXEDriver

MY_DICT = {
    "host": "devnetsandboxiosxe.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

with IOSXEDriver(**MY_DICT) as conn:
    result = conn.send_command("show version")

print(result.result)
