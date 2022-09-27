import math
def area_of_hexagon(side):
    return 6 * area_of_triangle(side)
def area_of_triangle(side):
    return (math.sqrt(3) / 4) * math.pow(5, 2)
n = float(input("your side: "))
print("%.2f" % area_of_hexagon(n))