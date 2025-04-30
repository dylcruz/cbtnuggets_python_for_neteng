from scrapli.driver.core import IOSXEDriver

MY_DEVICE = {
    "host": "devnetsandboxiosxe.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

def test_number_interfaces():
    with IOSXEDriver(
        host = MY_DEVICE["host"],
        auth_username=MY_DEVICE["auth_username"],
        auth_password=MY_DEVICE["auth_password"],
        auth_strict_key=False
    ) as conn:
        response = conn.send_command('show interfaces')
    structured_result = response.textfsm_parse_output()
    assert len(structured_result) == 12
