# a=int(input("Enter the 1st value :"))
# b=int(input("Enter the 2nd value :"))
# c= int(input("Enter the 3rd value :"))
# min= a if a<b and a<c else a if b<c else c
# print("the minumum value is:" , min)



# import math
# r=int(input("enter the raidus="))
# val=round(math.pi*r**2)
# print(val)




from sys import argv

sum =0 
print("the number of the object are in argv", len(argv))
agrs=argv[1:]
for  x in agrs:
    n=int(x)
    sum=sum+n
print ("the sum is ", sum)

