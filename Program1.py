def fact(n):
    c=1
    for i in range(1,n+1):
        c=c*i
    return c
inp=int(input("Enter the number: "))
print(fact(inp))
