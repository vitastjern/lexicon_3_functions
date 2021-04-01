# Write a function which receives three integernumbers and returns the smallest. 
# Use appropriate name for the function.

def smallest_of_three(a, b, c):
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c
    

first_int = int(input())
second_int = int(input())
third_int = int(input())

print(smallest_of_three(first_int, second_int, third_int))
