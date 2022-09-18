z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
p = []
n = []
for c in range(z):
    if x[c]<=0:
        n.append(x[c])
    else:
        p.append(x[c])
print('Second list: ', p)
print('Third list: ', n)