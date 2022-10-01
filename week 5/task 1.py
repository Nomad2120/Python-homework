import math
class Rectangle:
    def __init__(self, color="green", width=100, height=100):
        self.color = color
        self.width = width
        self.height = height
        self.diagonal = math.sqrt(math.pow(self.height, 2) + math.pow(self.width, 2))

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * (self.width + self.height))


rect1 = Rectangle()
print(rect1.color)
print(rect1.diagonal)
print(rect1.square())
print(rect1.perimeter())
rect2 = Rectangle("yellow", 23, 34)
print(rect2.color)
print(rect2.diagonal)
print(rect2.square())
print(rect2.perimeter())