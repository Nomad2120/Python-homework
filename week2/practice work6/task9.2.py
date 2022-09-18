z1=int(input("Your length of array:"))
l1=input("Your list:")
x1 = list(map(int, l1.split()))
z2=int(input("Your length of array:"))
l2=input("Your list:")
x2 = list(map(int, l2.split()))
x2,x1=x1,x2
print("List 1:",x1)
print("List 2:",x2)
