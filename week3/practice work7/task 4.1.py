import math
def dividing_by_fraction(lst):
    list_new1 = list(map(int, arr[0].split('/')))
    list_new2 = list(map(int, arr[1].split('/')))
    return irreducible_fraction([list_new1[0] * list_new2[1], list_new1[1] * list_new2[0]])

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
result = dividing_by_fraction(arr)
print(result[0], "/", result[1])