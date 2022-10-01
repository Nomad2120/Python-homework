class calculator():
    def sum(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        return (a/b)
x=int(input("Your value of x: "))
y=int(input("Your value of y: "))
print("Sum:",calculator.sum(x,y))
print("Difference:",calculator.subtract(x,y))
print("Multiplication:",calculator.multiply(x,y))
print("Division:",calculator.divide(x,y))