z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))

od= []

for c in range(z):
    if x[c] % 2 != 0:
        od.append(x[c])
od.sort(reverse=True)

if len(od)==0:
    print("no such numbers")
else:
    print("new array: ", od)