z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
absence = True
for c in range(z):
    for v in range(c+1,z):
        if x[c] == x[v]:
            absence = False
            print("dublicate:",x[c])
if absence == True:
    print("duplicate is absenced")