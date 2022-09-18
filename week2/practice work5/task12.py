z= str(input('Your text: '))
x=z.split()
for c in x:
    if c.endswith('i'):
        print(c, " ")