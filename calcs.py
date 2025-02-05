num1=eval(input("Enter the value 1: "))
opr=str(input("Enter the operation: "))
num2=eval(input("Enter the value 2: "))

if opr=="+":
    sum =num1+num2
    print("The result is:",sum)
elif opr=="-":
    sum=num1-num2
    print("The result is:",sum)
elif opr=="*":
    sum=num1*num2
    print("The result is:",sum)
elif opr=="/":
    sum=num1//num2
    print("The result is:",sum)
