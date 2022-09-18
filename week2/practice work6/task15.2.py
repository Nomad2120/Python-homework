z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
od = []

for i in range(z):
    if x[i] % 2 != 0:
        od.append(x[i])
od.sort(reverse=True)

if len(od)==0:
    print("There is no odd elements")
else:
    print("New list with odd elements ", od)