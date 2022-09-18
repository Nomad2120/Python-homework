def change(list):
    list[0], list[len(list) - 1] = list[len(list) - 1], list[0]
    return list
l = input("Your list: ")
x = list(map(str, l.split()))
print(change(x))