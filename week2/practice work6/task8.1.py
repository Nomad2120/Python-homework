z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
sum = 0
product = 1
for c in x:
    sum+= c
    product *= c
print("Sum of the elements:",sum)
print("Product of the element:",product)