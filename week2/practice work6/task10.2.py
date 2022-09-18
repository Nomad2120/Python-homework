z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
print(x)
for c in range(z):
    if x[c] < 10 :
       x[c] = 0
    elif x[c] > 20:
        x[c] = 1

print("new list:",x)