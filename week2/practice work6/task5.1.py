z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))

for c in range(z):
    for v in range(c+1,z):
        if x[c] == x[v]:
            if x[c] < 0 and x[v] < 0:
                print(x[c], x[v])