num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print('choose your action')
action=input('+,-,*,/')
if action == '+':
        print(num1, "+", num2, "=", num1 + num2)
elif action == '-':
        print(num1, "-", num2, "=", num1 - num2)
elif action == '*':
        print(num1, "*", num2, "=", num1 * num2)
elif action == '/':
        print(num1, "/", num2, "=", num1 / num2)
else:
     print("Error")