my_list_of_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_nums(num):
    if num % 2 == 0:
        return True
    else:
        return False

my_even_list_of_nums = list(filter(even_nums, my_list_of_nums))
print(my_even_list_of_nums)

my_list_of_interfaces = ['Gig0/0', 'Fa0/0', 'Gig0/1', 'Gig0/2', 'Loopback1', 'Portchannel1']

my_gig_interfaces = list(filter(lambda x: x.startswith("Gig"), my_list_of_interfaces))
print(my_gig_interfaces)