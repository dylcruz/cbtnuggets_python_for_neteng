# def regular_function(num1, num2):
#     """
#     Simple example of a regular function
#     """
    
#     result = num1 + num2
#     return result

# answer = regular_function(1, 2)
# print(answer)

adder = lambda num1, num2: num1 + num2
print(adder(1, 3))

high_low = lambda x: "The number is greater than 10" if x > 10 else "The number is not greater than 10"

print(high_low(11))

exponential = lambda x, y=2: x ** y

print(exponential(3))
print(exponential(3,3))
