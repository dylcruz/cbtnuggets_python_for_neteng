def square_me(list_of_nums):
    my_list = []
    for num in list_of_nums:
        my_list.append(num * num)
    return my_list

squared_list = square_me([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(squared_list)

def square_me(list_of_nums):
    for num in list_of_nums:
        yield (num * num)

gen_object = square_me([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print(gen_object)

for i in gen_object:
    print(i)

my_list_comp = [num * num for num in range(5,10)]
print(my_list_comp)

my_gen_comp = (num * num for num in range(5,10))
print(my_gen_comp)
