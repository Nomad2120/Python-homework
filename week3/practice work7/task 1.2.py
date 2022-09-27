import numpy
def sum_and_mean(arr):
    list_new = list(map(int, arr.split()))
    sum1 = sum(list_new)
    mean = numpy.mean(list_new)
    print("array",list_new,",sum of elements:",sum1,".Mean :",mean)
n = int(input("your number of arrays:"))
arrList = []
for i in range(n):
    arrList.append(input("your the array :"))
for i in range(n):
    sum_and_mean(arrList[i])