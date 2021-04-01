# Write a function that receives two characters and returns a single string with all 
# the characters in between them according to the ASCII code.
# (Don't include the given characters in the string)

def ascii_str(first, last):
    my_str = ""
    for x in range(ord(first)+1, ord(last)):
        
        if x > ord(first)+1:
            my_str = my_str + " "

        my_str = my_str + chr(x) 
    
    return my_str


frst = input()
scnd = input()
print(ascii_str(frst, scnd))

