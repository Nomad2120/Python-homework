def diagonal(a):
    n = 3

    for col in range(n):

        startcol = col
        startrow = 0

        while (startcol >= 0 and
               startrow < n):
            print(a[startrow][startcol], end=" ")

            startcol -= 1
            startrow += 1

        print()

    for row in range(1, n):
        startrow = row
        startcol = n - 1

        while (startrow < n and
               startcol >= 0):
            print(a[startrow][startcol],
                  end=" ")

            startcol -= 1
            startrow += 1

        print()


a= [[7, 13, 2],
    [5, 5, 1],
    [4, 13, 17]]

diagonal(a)