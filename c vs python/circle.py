""" import math as M
radious=float(input("Enter radious for calculate area: "))
area=M.pi*radious*radious
circumferece=2*M.pi*radious
print("The circumference of circle is :%.3f"%circumferece)
print("The area of the circle is :%.2f"%area)
# print("The area of the circle is :",area) """


# class base 
class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14*(self.radius**2)
obj=circle(3)
print("Area of circle: ",obj.area())




# radious=int(input("Enter radious for calculate area: "))
# area=3.14159*radious*radious
# print(area)



""" pi=3.14159
def area_of_circle(r):
    return pi*r**2

radious=int(input("Enter radious for calculate area: "))
print("The area of circle is :",area_of_circle(radious)) """