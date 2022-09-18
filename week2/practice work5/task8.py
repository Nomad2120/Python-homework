z=str(input('Your text:'))
x=0
for c in z:
    if c==' ':
        x+=1
    if c=='.':
        break
print("Number of words:",x+1)