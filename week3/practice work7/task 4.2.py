import math
def inside_the_circle(x, y, radius):
    if math.pow(x, 2) + math.pow(y, 2) <= pow(radius, 2):
        return True
R = input("your R of circle: ")
wannaExit = False
while(wannaExit!=True):
    x, y = list(map(int, input("your x,y of point").split()))
    wannaExit = bool(input("wanna exit?"))
    inside_the_circle(x, y, R)