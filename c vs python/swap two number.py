#swap two number using class
class Number:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def swap(self):
        temp=self.x
        self.x=self.y
        self.y=temp
    def display(self):
        print("After swap a is %d and b is %d"%(self.x,self.y))
        
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
obj=Number(num1,num2)
obj.swap()
obj.display()



#swap two number using + or - operator 
""" num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num1=num1+num2
num2=num1-num2
num1=num1-num2
print("Swapped values of x is %d and y is %d"%(num1,num2)) """



# swap two numbers 

""" num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num1,num2=num2,num1
print("FIrst number:",num1)
print("second number:",num2) """


# swap two numbers in a list
""" def swapIndex(list, index1, index2):
	list[index1], list[index2] = list[index2], list[index1]
	return list
List = [25, 85, 30, 40]
index1, index2 = 2, 4
# index1, index2 = 1, 3
print(swapIndex(List, index1-1, index2-1)) """


#swap two number using function
""" def swapNumber(a,b):
    temp=a
    a=b
    b=temp
    return a,b
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
print("Before swapping :",num1,num2)
print("After swapping :",swapNumber(num1,num2)) """



#swap two number without using third variable
""" num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num1=num1*num2
num2=num1/num2 
#num2=num1//num2  #floor division
num1=num1/num2 
#num1=num1//num2
print("After swapping first number is %d and second number is %d"%(num1,num2)) """


#swap two number using bitwise XOR
""" num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num1=num1 ^ num2
num2=num1^num2
num1=num1^num2
print("After swapping the first number is %d 2nd number is %d"%(num1,num2)) """


