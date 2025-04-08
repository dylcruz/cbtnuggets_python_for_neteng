from datetime import datetime
from scrapli.driver.core import IOSXEDriver

my_time = datetime.now().strftime("%H:%M:%S")
print(my_time)

command_to_send = input('Enter the command you wish to send: ')

MY_DEVICE = {
    "host": "devnetsandboxiosxe.cisco.com",
    "auth_username": "admin",
    "auth_password": "C1sco12345",
    "auth_strict_key": False,
}

with IOSXEDriver(**MY_DEVICE) as conn:
    result = conn.send_command(command_to_send)

result_list = result.result.splitlines()

with open(f"{command_to_send}-{my_time}.txt", "x") as file:
    for line in result_list:
        file.write(line + '\n')
