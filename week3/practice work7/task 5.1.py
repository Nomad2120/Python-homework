import math
import numpy
def substract(lst):
    list_new1 = list(map(int, arr[0].split('/')))
    list_new2 = list(map(int, arr[1].split('/')))
    result = [((numpy.lcm(list_new1[1], list_new2[1]) / list_new1[1]) * list_new1[0]) - (
            (numpy.lcm(list_new1[1], list_new2[1]) / list_new2[1]) * list_new2[0]),
              numpy.lcm(list_new1[1], list_new2[1])]

    if (result[0] == 0):
        print(result[0])
    else:
        print(result[0], "/", result[1])

def irreducible_fraction(lst):
    divider, x, y = Euclid_algorithm(lst[0], lst[1])
    return [i / divider for i in lst]

def Euclid_algorithm(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = Euclid_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

arr = []
for i in range(2):
    arr.append(input("your fraction n" + str(i + 1) + ": "))
substract(arr)