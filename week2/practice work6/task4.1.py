z = [17, 51, -23, 12, -7, 13, 0, -7, 78, 65, 17, 53]
print(max(z))
for c in range(len(z)):
    if z[c] == min(z):
        print(c)