import math

x, y, z = 2, 1, 3
result = ((math.fabs((math.log(x**3))) + math.exp(2 * x)) / (x + 3.4)) - 1/(math.tan((3 / (x * y * z))) ** 3)
print('%.2f' % result)
