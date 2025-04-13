from time import perf_counter

def performance_test(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        finish = perf_counter()
        print(f'Execution time: {finish - start}')
    
    return wrapper

@performance_test
def print_some_numbers(num):
    for i in range(0, num):
        print(i)

print_some_numbers(1000000)
