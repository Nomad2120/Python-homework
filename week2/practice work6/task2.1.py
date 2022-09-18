z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
print("Min element in array:",min(x))
for c in range(z):
    if x[c] == min(x):
        print("Index of min element:",c)