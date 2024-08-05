operator= input("Enter the operator[ + ,- , / , * ]: ")
num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
a=0
if operator == '+':
    a =num1+num2
    print("result: ",a)
elif operator == '-':
    a=num1-num2
    print("result: ",a)
elif operator == '*':
    a=num1*num2
    print("result: ",a)
elif operator == '/':
    a=num1/num2
    print("result: ",a)
else:
    print("invalid operator")



