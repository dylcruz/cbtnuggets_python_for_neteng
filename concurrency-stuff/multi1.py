from multiprocessing import Process
from time import perf_counter
from scrapli.driver.core import IOSXEDriver
from inv import DEVICES

start = perf_counter()

def send_cmd(device):
    print(f'\n\nSENDING COMMAND TO DEVICE {device["hostname"]}')
    with IOSXEDriver(
        host=device['host'],
        auth_username='xdyldogx',
        auth_password='NI-Mi6F8bpKC_4qv',
        auth_strict_key=False,
    ) as conn:
        response = conn.send_command('show version')
        print(response.result)
    print(f'DONE WITH {device["hostname"]}')

if __name__ == '__main__':
    processes = []

    for device in DEVICES:
        proc = Process(target=send_cmd, args=(device,))
        processes.append(proc)

    for proc in processes:
        proc.start()

    for proc in processes:
        proc.join()

    end = perf_counter()
    print(end - start)
