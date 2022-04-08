s=input("Enter the string: ")
s=s.split()
l=[]
for i in s:
    if i.isdigit():
        l.append(i)
print(l)

