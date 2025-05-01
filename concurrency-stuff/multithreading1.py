import threading
from time import perf_counter
from scrapli.driver.core import IOSXEDriver
from inv import DEVICES

start = perf_counter()

threads = []

def send_cmd(device):
    with IOSXEDriver(
        host=device['host'],
        auth_username='xdyldogx',
        auth_password='NI-Mi6F8bpKC_4qv',
        auth_strict_key=False,
    ) as conn:
        response = conn.send_command('show version')
        print(response.result)

if __name__ == '__main__':
    for device in DEVICES:
        th = threading.Thread(target=send_cmd, args=(device,))
        threads.append(th)
    
    for th in threads:
        th.start()

    for th in threads:
        th.join()

    end = perf_counter()

    print(end - start)
