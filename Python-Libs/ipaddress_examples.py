import ipaddress

network = ipaddress.ip_network("192.168.1.0/28")

for host in network.hosts():
    print(host)

my_ip = ipaddress.ip_address("10.0.0.1")
print(my_ip.is_global)
print(my_ip.is_private)

test1 = ipaddress.ip_network("192.168.1.1/30", strict=False)
test2 = ipaddress.ip_network("192.168.1.2/30", strict=False)

if test1 == test2:
    print('True')
else:
    print('False')
