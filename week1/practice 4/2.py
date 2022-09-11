seq_of_int=[17, 2, 13, 1, 3, 4, 5, 7, 8,0]
sum, i=0,0
while seq_of_int[i] !=0:
    sum+=seq_of_int[i]
    i+=1
print('the sum of all numbers in the sequence:',sum)
print('the number of all numbers in the sequence:',i+1)
