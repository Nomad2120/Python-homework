num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print('choose your action')
action=input('+,-,*,/')
res=0
if action == '+':
 res=num1+num2
elif action == '-':
 res=num1-num2
elif action == '*':
 res=num1*num2
elif action == '/':
    if (num2 == 0):
        print('invalid action')
        res=num1/num2
else:
     print("Error")
print(num1,action,num2,'=',res)