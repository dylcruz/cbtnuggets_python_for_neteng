from functools import reduce

my_list_of_nums = [0, 1, 2, 3, 4, 5]

def adder(x, y):
    result = x + y
    return result

print(reduce(adder, my_list_of_nums))

my_random_nums = [11, 2, 5, 66, 43, 28]
print(reduce(lambda x, y: x if x > y else y, my_random_nums))
