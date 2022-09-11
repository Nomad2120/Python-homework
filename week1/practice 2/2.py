import math
y=int(input('enter the var y:'))
x=int(input('enter the var x:'))
h=math.sqrt(math.cos(2 * y) + math.sin(4 * y) + math.sqrt(math.exp(x) + math.exp(-x))) / math.pow((math.exp(x) + math.exp(-x)), 3) * math.pow((math.sin(4 * y) + math.cos(2 * y) - 2), 2)
print('your solution'+ format(h))
