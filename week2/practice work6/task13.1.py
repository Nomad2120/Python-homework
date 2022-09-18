z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
absence = True
for c in range(z):
    for v in range(c + 1, z):
        if x[c] == x[v]:
            absence = False
            print("Dublicate is:", x[c])
            print("It's indices is:",c,v)
if absence == True:
    print("Duplicate is absence")