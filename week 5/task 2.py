class name:
    def __init__(self, first_name, last_name, full_name):
        self.first_name = first_name.capitalize()
        self.last_name = last_name.capitalize()
        self.full_name = full_name.title()

a = str(input('Your first name: '))
b = str(input('Your last name: '))
c = []
c.append(a)
c.append(b)
d = ' '
for i in c:
    d += ' ' + i
person = name(a, b, d)
print(person.first_name)
print(person.last_name)
print(person.full_name)