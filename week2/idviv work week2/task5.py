import math
z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
def list_sort():
    for i in range(z):
        math.fabs(x[i])
    x.sort(reverse=True)
    print(x)
list_sort()