# Write a function that checks if a given password is valid. Password validations are:
# • The lengthshould be 6 -10 characters (inclusive)
# • It should consists only letters and digits 
# • It should have at least 2 digits 
# 
# If a password is valid print "Password is valid".
#
# If it is NOT valid, for every unfulfilled rule print a message:
#       • "Password must be between 6 and 10 characters"
#       • "Password must consist only of letters and digits"
#       • "Password must have at least 2 digits"

def chk_pwd(pwd):

    digit_count = 0     # need to be at least 2 digits
    valid_pwd = True

    if (len(pwd) < 6 or len(pwd) > 10):
        print("Password must be between 6 and 10 characters")
        valid_pwd = False


    if not pwd.isalnum():
        print("Password must consist only of letters and digits")
        valid_pwd = False

    for x in pwd:
        if x.isdigit():
            digit_count += 1

    if digit_count < 2:
        print("Password must have at least 2 digits")
        valid_pwd = False

    if valid_pwd:
        print("Password is valid")


my_pass = input()
chk_pwd(my_pass)
