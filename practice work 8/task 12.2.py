def subtract_last(matrix):
    for i in range(0, len(matrix) - 1):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j] - matrix[len(matrix) - 1][j]
    return matrix


n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

a = subtract_last(matrix=a)
for i in range(n):
    for j in range(m):
        print(a[i][j], end=' ')
    print()
