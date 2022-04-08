import re

inp = input("Enter the passwords(Each seperated by ,) : ")
passwords = inp.split(",")

Valid_Passwords = []
for i in passwords:
    
    if (len(i) > 6 ) and (len(i) < 12) and re.search("([a-z])+", i) and re.search("([A-Z])+", i) and re.search("([0-9])+", i) and re.search("([$#@])+", i):
        Valid_Passwords.append(i)
print("Valid Passwords are : ",end="")
print((" ").join(Valid_Passwords))
