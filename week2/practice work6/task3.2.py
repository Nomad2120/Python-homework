z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
for c in range(z):
    if x[c] < 15:
        x[c] = x[c] * 2
print("Final array is :", x)
