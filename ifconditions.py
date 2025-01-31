# name=input("enter your name: ")
# if name=="manoj":
#     print("hi good morning manoj")
# else: print("hi good moring", name)


# 1)write a program to check the wheather person is eligible to vote or not : (accept the age from the user )

# name=input("Enter you name: ")
# age=eval(input("enter your current age: "))
# print(type(name))
# print(type(age))

# if age <= 18:
#     print(name, "your not egliable to voteing")
# else:
#     print(name,"your egliable for voteing")

#2) write a program to check whather a number entered by user is even or odd 

# value=eval(input("enter the Value: "))
# if value%2==0:
#     print("Enter number is EVEN")
# else:
#     print("Enter number is ODD")

#3) write a program to check whether a number is divisible by 7 or not .

# number=int(input("Enter the number: ") )
# if number%7==0:
#     print("The Number can be divided by 7")
# else:
#     print("The Number can not be divided by 7")


#4) write a program to display "hello" if a number entered by user is a multiple of 5, otherwise print bye.

# number=int(input("Enter the Number: "))
# if number%5==0:
#     print("HELLO")
# else:
#     print("BYE")

# 5) 
# units=int(input("Enter the units: "))

# amt=0
# if units<=100:
#     amt=0
# if units>100 and units<200:
#     amt=(units-100)*5
# if units>200:
#     amt=500+(units-200)*10
# print("Amount to be paied is Rs:", amt)

# **  if-elif-elif -else

# writing a code foe the confition 

# brand = str(input("Enter your fav Brand: "))

# if brand=="puma":
#     print("your fav brand is ", brand)
# elif brand =="reebook":
#     print("your fav brand is ",brand)    
# elif brand=="aadias":
#     print("you fav brand is ", brand)
# else:
#     print("none of this ur fav brand...!")    


# write a program  to find the biggest  of the given two numbwe in the commadn prompt


# num1=eval(input("Enter the 1st number: "))
# num2=eval(input("enter the 2nd number: "))  
# if num1>num2:
#     print("Biggest number is:", num1)   
# else:
#     print("Biggest number is :", num2)
    
 # write a program  to find the biggest  of the given 3 numbwe in the commadn prompt   
    
# num1=eval(input("Enter the 1st number: "))
# num2=eval(input("enter the 2nd number: "))
# num3=eval(input("enter the 3rd number: "))
  
# if num1>num2 and num1>num3:
#     print("Biggest number is:", num1)   
# elif num2>num3:
#     print("Biggest number is:", num2)
# else:
#     print("Biggest number is :", num3)


#write a program to find the smallest number of the given 2 numbers 

# n1=int(input("Enter the 1st number: "))
# n2=int(input("Enter the 2nd number: "))
# if n1<n2:
#     print("smallest number is:",n1)
# else:
#     print("smalles number is:", n2)


#write a program to find the smallest number of the given 3 numbers 
number1=eval(input("Enter the 1st number:"))
number2=eval(input("Enter the 2nd number:"))
number3=eval(input("Enter the 3rd number:"))
if number1<number2 and number1<number3:
    print("smallest number is:", number1)
elif number2<number3:
    print("smallest number is:", number2)
else:
    print("smallest number is:", number3)