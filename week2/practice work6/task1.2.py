z = [17, 23, 2, 0, 2, 13, 0, 9]
x = 0
for c in z:
    x += c
mean = (x/(len(z)+1))
for c in range(len(z)):
    if z[c] == 0:
        z[c] = mean
print(mean, z)