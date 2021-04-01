# You will receive a single number. You have to write a function that returns the
# sum of all even and all odd digits from that number as a single string like in 
# the examples below. 

def sum_odd_even(number_string):
    odd = 0
    even = 0
    for x in number_string:
        y = int(x)          # vill inte typecasta så mycket...
        if y % 2 == 0:
            even += y
        else:
            odd += y

    return "Odd sum = " + str(odd) + ", Even sum = " + str(even)


some_number_str = input()
print(sum_odd_even(some_number_str))
