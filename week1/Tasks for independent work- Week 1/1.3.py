import math
a = float(input('enter the numb a'))
print(round(math.floor(a) / 100 + (a % 1) * 100, 2))