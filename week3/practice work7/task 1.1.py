def area_shapes():
    choose = input("what shape you want to calc: ")
    area = 0
    pi = 3.14
    if choose == "square":
        side = int(input("side: "))
        area = area + (side ** 2)
    elif choose == "circle":
        radius = int(input("radius: "))
        area = area + (2 * pi * radius)
    elif choose == "rectangle":
        length = int(input("length: "))
        width = int(input("width: "))
        area = area + (length * width)
    elif choose == "triangle":
        base = int(input("base: "))
        height = int(input("height: "))
        area = area +(0.5 * base * height)
    else:
        print ("This is incorrect value")
    print ("%.2f" % area)

area_shapes()