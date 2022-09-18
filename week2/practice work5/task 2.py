z=str(input('Your text:'))
x=0
for c in z:
    if c == ':':
        x += 1
        z=z.replace(c, '%')
print('Your changed text:',z)
print(x)
