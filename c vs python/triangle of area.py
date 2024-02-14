# find area using herons formula
import math
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
s=(a+b+c)/2.0
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("The area of herons formula in triangle :",area)



# base=int(input("enter base to calculate area of triangle :"))
# height=int(input("enter height to calculate area of triangle :"))
# area=.5*base*height
# print("The area of triangle is :"+str(area))