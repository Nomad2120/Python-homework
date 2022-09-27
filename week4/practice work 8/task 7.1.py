def lower_t(a, row, col):
    for i in range(0, row):

        for j in range(0, col):

            if i < j:

                print("0", end=" ")

            else:
                print(a[i][j],
                      end=" ")

        print(" ")


def upper_t(a, row, col):
    for i in range(0, row):

        for j in range(0, col):

            if i > j:
                print("0", end=" ")

            else:
                print(a[i][j],
                      end=" ")

        print(" ")


a = [[7, 13, 2],
          [5, 5, 1],
          [4, 13, 17]]
row = 3
col = 3

print("Your lower triangular matrix: ")
lower_t(a, row, col)

print("Your upper triangular matrix: ")
upper_t(a, row, col)