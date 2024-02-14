""" 
student,teacher,class,  .ekhane protitai ek ekta object 
object oriented programming,procedural programming ,functional programming 
beginer hesebe oop diye suru kora valo ....object er moddhe kisu data and kisu action thake 
object oriented bolte object gular moddhe relation thakbe seta hoite pare 1 to many,many to 1...
OOP weekipedia search ....what are the pilars of oop -> inheritance,encapsulation,polymorphism ,abstraction  


"""


# Ena poribohon

class Company:
    def __init__(self,name,address) -> None:
        self.name=name
        self.bus=[] # amader bus,routes,drivers,counter,manager,supervisor and fare thakbe 
        self.routes=[]
        self.drivers=[]
        self.counter=[]
        self.manager=[]
        self.supervisor=[]
        self.fare=[] # buser vara koto 

class Driver:
    def __init__(self,license,name,age) -> None:
        self.license=license
        self.name=name 
        self.age=age

class Counter:
    def __init__(self) -> None:
        pass
    def purchase_a_ticket(self,start,destination):
        pass 

class Passenger:
    pass

class Supervisor:
    pass

rahim=Driver('a')