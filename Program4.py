num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
o=input(" For Addition +\nFor Substraction -\nFor Multiplication *\nFor Division /\nSelect the operation: ")
if o=="+":
    print('{} + {} = '.format(num1, num2),end="")
    print(num1 + num2)
elif o=="-":
    print('{} - {} = '.format(num1, num2),end="")
    print(num1 - num2)
elif o=="*":
    print('{} * {} = '.format(num1, num2),end="")
    print(num1 * num2)
elif o=="/":
    print('{} / {} = '.format(num1, num2),end="")
    print(num1 / num2)
else:
    print("Invalid Operation").py
