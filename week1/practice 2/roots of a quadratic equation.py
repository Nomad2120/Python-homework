import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = ((b**2) - (4*a*c))
if d>0: 
        print((-b + math.sqrt(d))/(2 * a))
        print((-b - math.sqrt(d))/(2 * a))
elif d==0:
        print((-b)/2*a)
else:
        print("No roots")
