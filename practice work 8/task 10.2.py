def asc_kth(m):
    for i in range(len(m)):

        for j in range(len(m[i])):

            for k in range(len(m[i]) - j - 1):

                if m[i][k] > m[i][k + 1]:

                    t = m[i][k]
                    m[i][k] = m[i][k + 1]
                    m[i][k + 1] = t

    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


m = [[17, 13, 7, 1], [7, 21 , 1, 7], [13, 5, 1, 2], [7, 3, 8, 2]]
asc_kth(m)