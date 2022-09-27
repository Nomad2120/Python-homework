n = 4


def printmatrix(a):
    i = None
    j = None
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=" ")
        print('')


def kth(arr, n, z):
    arr.sort()

    return arr[z - 1]


def dividebydiag(a, z):
    i = None
    j = None
    arr = [0] * n

    for i in range(n):
        for j in range(n):
            arr[j] = a[i][j]
        a[i][i] = kth(arr, n, z)
    printmatrix(a)


a = [[17, 13, 5, 7], [2, 5, 3, 8], [13, 21, 1, 6], [7, 5, 10, 8]]

z = 3
dividebydiag(a, z)