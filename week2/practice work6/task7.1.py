z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
sum = 0
odd = 1
for c in range(z):
    if x[c] % 2 != 0:
        odd *= x[c]
    else:
        sum+=x[c]
print("Sum of even elements:",sum)
print("Product of odd elements:",odd)