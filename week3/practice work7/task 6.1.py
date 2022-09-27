def Euclid_algorithm(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = Euclid_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def lcm(a, b):
    gcd, x, y = Euclid_algorithm(a, b)
    return (a * b) / gcd

a, b = list(map(int, input("your a,b: ").split()))
gcd, x, y = Euclid_algorithm(a, b)
print("GCD is:", gcd)
print("LCM is:", lcm(a, b))