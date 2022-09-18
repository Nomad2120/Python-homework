z= str(input('Your text: '))
x = z.split()
for c in x:
    if c[len(c) - 1] == "i":
        print(c, end=" ")
    elif c[0] == "a":
        print(c, end=" ")