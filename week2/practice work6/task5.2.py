z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))

x = list(dict.fromkeys(x))
print(x)