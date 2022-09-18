z = [1,2,3,4,5,6,7,8,9]
res = 0
for c in range(len(z)):
    if z[c] % 2 != 0:
        res += z[c]
print("The list:",z)
print("Sum of odd elements:",res)