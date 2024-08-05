operator= input("Enter the operator[ + ,- , / , * ]: ")
n=int(input("Enter number of operands to perfrom calculation: "))
result=[]
for i in range(n):
    num=float(input("Enter number: "))
    result.append(num)

if operator == '+':
    a =0
    for num in result:
        a += num
    print("result: ",a)
elif operator == '-':
    a =result[0]
    for num in result[1:]:
        a -= num
    print("result: ",a)
elif operator == '*':
    a =1
    for num in result:
        a *= num
    print("result: ",a)
elif operator == '/':
    a =result[0]
    for num in result[1:]:
        a /= num
    print("result: ",a)
else:
    print("invalid operator")



