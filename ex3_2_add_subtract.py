# You will receive three integer numbers. Write a function sum_numbers() to get the
# sum of the first two integers and subtract() function that subtracts the third 
# integer from the result. Wrap the two functions in a function called 
# add_and_subtract() which will receive the three numbers.

def sum_numbers(a, b):
    return a+b


def subtract(a, b):
    return a-b


def add_and_subtract(a, b, c):
    return subtract(sum_numbers(a,b), c)


first = int(input())
second = int(input())
third = int(input())

print(add_and_subtract(first, second, third))
