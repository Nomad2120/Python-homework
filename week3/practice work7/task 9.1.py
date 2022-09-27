def sum_digit(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

def substract(n, sum):
    repeat = -1
    while n >= 0:
        n -= sum
        repeat += 1
    return repeat

n = int(input("your number: "))
sum = sum_digit(n)
print(sum)
print( substract(n, sum))