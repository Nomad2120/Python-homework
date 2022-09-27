def twins(n):

    if n <= 1:
        return False

    for i in range(3, n):
        if n % i == 0:
            return False

    return True


def printTwins(n):
    for i in range(n, n * 2):
        if twins(i):
            print(i, end=" ")


n = int(input("enter the n: "))
printTwins(n)