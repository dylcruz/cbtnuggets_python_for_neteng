def test_func(device, command):
    print(f'Sending {command} to {device}')

breakpoint()
test_func('R1', 'show run')
