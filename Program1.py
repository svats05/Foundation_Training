def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

inp=int(input("Enter the number: "))
print(fact(inp))
