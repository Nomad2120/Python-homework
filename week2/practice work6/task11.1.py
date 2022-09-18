z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
b = False
x.sort()
for c in reversed(x):
    if c%2 == 0:
        print(c)
        break