class Family:
    def __init__(self,address) -> None:
        self.address=address

class School:
    def __init__(self,id,level) -> None:
        self.id=id
        self.level=level

class Sport:
    def __init__(self,game) -> None:
        self.game=game

# ekhane student class ta tar family,school,and sport k inherit korbe eta hocche multiple inheritance
class Student(Family,School,Sport):
    def __init__(self, address,id,level,game)-> None:
        School.__init__(self,id,level)
        Sport.__init__(self,game)
        Family.__init__(self,address)# every class k init korte hobe 
        super().__init__(address)


""" 
class & object ....attributes and methods
OOP -> inheritance, encapsulation , polymorphism , abstraction...

interview question.... abstract class and interface er difference 

class->> private,public ,protected
"""