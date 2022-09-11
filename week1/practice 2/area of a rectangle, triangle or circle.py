import math
print("1.Rectangle")
print("2.Triangle")
print("3.Circle")
area=0.0
while(1):
    choice=int(input("Enter your choice:"))
    if choice==1:
        l=float(input("Enter length:"))
        w=float(input("Enter width:"))
        area=l*w
        print("Area of rectangle is:%.2f"%area)
    elif choice==2:
        a=float(input("a="))
        b=float(input("b="))
        c=float(input("c="))
        p=(a+b+c)/2
        s=math.sqrt(p*(p-a)*(p-b)*(p-c))
        print("Area of the triangle is:%.2f"%s)
    elif choice==3:
        r=float(input("Enter radius:"))
        area=3.14*r*r
        print("Area of the Cicle is:%.2f"%area)
    else:
        print("Bruh, are you kidding me?")
        
        
