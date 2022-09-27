def max_element(lst):
    return max(lst)

arr = input("Your array: ")
list1 = list(map(int, arr.split()))
print("Your maximum of 1st list:", max_element(list1))

arr = input("Enter the array: ")
list2 = list(map(int, arr.split()))
print("Your maximum of 2nd list:", max_element(list2))

index1 = list1.index(max_element(list1))
index2 = list2.index(max_element(list2))

list1[index1], list2[index2] = list2[index2], list1[index1]

print(list1, list2)