import math
z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
print(math.fabs(min(x)))
x.reverse()
print(x)