z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(int, l.split()))
x.sort()
print("Max element in list: ", x[z-1])
x.sort(reverse=True)
print("Min element in list: ", x[z-1])