def swap(lst):
    lst[0],lst[len(lst)-1] = lst[len(lst)-1],lst[0]
    return lst
input("Your length of array: ")
list_new = list(map(int, (input("Your array: ")).split()))
print("unchaged: ",list_new)
print("changed: ",swap(list_new))