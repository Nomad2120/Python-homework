import math
def area_quadrilateral(lst, diagonal):
    h1 = 2 * (area_of_Triangle(lst[0], lst[1], diagonal) / diagonal)
    h2 = 2 * (area_of_Triangle(lst[2], lst[3], diagonal) / diagonal)
    area = 0.5 * diagonal * (h1 + h2)
    return area


def area_of_Triangle(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


x = list(map(float, input("your 4 sides one after one: ").split()))
d = float(input("your diagonal: "))
print("your area of quadrilateral: ", area_quadrilateral(x, d))