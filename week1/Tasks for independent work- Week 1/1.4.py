import math
a = float(input('Enter the value for a'))
y = ((a ** 2) / 3) + (((a ** 2) + 4) / 6) + (math.sqrt((a ** 2) + 4) / 4) + (math.sqrt(((a ** 2) + 4) ** 3) / 4)
print("%.2f" % y)