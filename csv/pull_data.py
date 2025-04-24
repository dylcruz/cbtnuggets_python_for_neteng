import csv
from rich import print as rprint
from scrapli.driver.core import IOSXEDriver
from inv import DEVICES

for device in DEVICES:
    hostname = device['hostname']
    with IOSXEDriver(
        host = device['host'],
        auth_username='admin',
        auth_password='C1sco12345',
        auth_strict_key=False
    ) as conn:
        response = conn.send_command('show version')
    
    structured_results = response.textfsm_parse_output()[0]
    version = structured_results['version']
    serial = structured_results['serial']
    # rprint(f'{hostname} - {version} - {serial}')
    with open('test.csv', 'a') as csv_data:
        writer = csv.writer(csv_data)
        my_data = ("dylcruz", hostname, serial[0], version)
        writer.writerow(my_data)
