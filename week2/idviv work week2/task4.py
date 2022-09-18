z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
b=int(max(x))
n=b/z
print("The result is:",n)