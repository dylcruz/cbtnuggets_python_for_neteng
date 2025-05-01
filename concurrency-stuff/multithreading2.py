from concurrent.futures import ThreadPoolExecutor
from scrapli.driver.core import IOSXEDriver
from time import perf_counter
from inv import DEVICES

start = perf_counter()

def send_cmd(device):
    with IOSXEDriver(
        host=device['host'],
        auth_username='xdyldogx',
        auth_password='NI-Mi6F8bpKC_4qv',
        auth_strict_key=False,
    ) as conn:
        response = conn.send_command('show version')
        return response.result

if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        results = executor.map(send_cmd, DEVICES)

    for result in results:
        print(result)

    end = perf_counter()

    print(end - start)
