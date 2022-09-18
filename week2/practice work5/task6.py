z=str(input('Your text:'))
x=0
for c in z:
    if c=="a":
        z=z.replace(c,"")
        x+=1
print("Your changes text:",z)
print(x)