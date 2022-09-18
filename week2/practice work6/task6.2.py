z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
res = 0
for c in range(z):
    if x[c] > 5:
        res += x[c]
print("Sum:",res)