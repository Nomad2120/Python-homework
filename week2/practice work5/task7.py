z=str(input('Your text:'))
x=round(len(z)/2)
print(x)
for c in range(x):
    z=z.replace('n','*',1)
print("Your changes text:",z)
