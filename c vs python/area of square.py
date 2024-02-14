# side=int(input("Enter the side of square: "))
# area=side*side
# # print("Area of square= ",area)
# print("Area of square= "+str(area))



""" def areaOfRectangle(width,height):
    area=width*height
    perimeter=2*(width+height)
    print("The area of Rectangular is :"+str(area))
    print("The perimeter of Rectangular is :",perimeter)
width=float(input("Enter width of rectangle:"))
height=float(input("Enter height of rectangle:"))
areaOfRectangle(width,height) """



class Rectangle:
    def __init__(self,w,h):
        self.width=w
        self.height=h
        
    def areaOfRectangle(self):
        return self.width*self.height
    def perimeterOfRectangle(self):
        return 2*(self.height+self.width)
obj=Rectangle(4,5)
print("Area of rectangle:",obj.areaOfRectangle())
print("Perimeter of rectangle:",obj.perimeterOfRectangle())
