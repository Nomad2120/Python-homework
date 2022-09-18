z=int(input("Your length of array:"))
l=input("Your list:")
x = list(map(str, l.split()))
def all_eq(x):
    q = []
    m = len(max(x, key = len))
    for c in x:
        if len(c) != m:
            for h in range(m-len(c)):
                c = c + "_"
            q.append(c)
        else:
            q.append(c)
    print(q)

all_eq(x)