z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
b = []
for c in x:
    if c < 10:
        if c % 2 == 0:
            b.append(c)
if len(b) == 0:
    print("There is no such elements")
else:
    print(b)