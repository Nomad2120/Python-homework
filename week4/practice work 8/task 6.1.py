MAX = 100
def sm_row(a, n, m):
    print("{", end="")
    for i in range(n):

        min = a[i][0]

        for j in range(1, m, 1):

            if (a[i][j] < min):
                min = a[i][j]

        print(min, end=",")

    print("}")

def sm_column(a, n, m):
    print("{", end="")
    for i in range(m):

        min = a[0][i]

        for j in range(1, n, 1):

            if a[j][i] < min:
                min = a[j][i]

        print(min, end=",")

    print("}")

n = 3
m = 3
a = [[7, 13, 2],
        [5, 5, 1],
        [4, 13, 17]]

print("smallest element of each row is", end=" ")
sm_row(a, n, m)
print("smallest element of each column is", end=" ")
sm_column(a, n, m)