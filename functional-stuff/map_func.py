my_list = [2, 4, 6, 8, 10]

def squared(num):
    return num ** 2

my_list_squared = map(squared, my_list)
print(list(my_list_squared))


my_new_list = [2, 4, 6, 8, 10]

my_new_list_squared = list(map(lambda x: x **2, my_new_list))
print(my_new_list_squared)

my_words = ['john', 'Paul', 'lauren', 'Trevor', 'simona']
my_new_words = list(map(lambda x: x.capitalize(), my_words))
print(my_new_words)
