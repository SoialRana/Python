""" ekhane area method ta various class e various shape nicche jemon rectangle er khetre area ja result dekhabe 
    circle er khetre area kintu same result dekhabe na ...tie amra bolte pari j area method ta various class e various 
    shape e nibe jetake amra boli many shape newa or polymorphism ..
"""

from math import pi

class Shape:
    def __init__(self,name) -> None:
        self.name=name

class Rectangle(Shape):
    def __init__(self, name,length,width) -> None:
        self.length=length
        self.width=width
        super().__init__(name)

    def area(self):
        return self.length*self.width
    
class Circle(Shape):
    def __init__(self, name,radius) -> None:
        self.radius=radius
        super().__init__(name)

    def area(self):
        return pi*self.radius*self.radius
    

