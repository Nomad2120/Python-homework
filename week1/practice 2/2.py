import math
y=int(input('enter the var y:'))
x=int(input('enter the var x:'))
h=(math.sqrt(math.cos(2*y)+(2*(math.sin(2*y)*math.cos(2*y))+math.sqrt(math.pow(math.e,x))+math.pow(math.e,-x)))/((math.pow(math.e,-x))+math.pow(math.e,x))**3*(2*(math.sin(2*y)*math.cos(2*y))+math.cos(2*y)-2)**2)
print('your solution'+ format(h))
