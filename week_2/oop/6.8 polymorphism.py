#poly--> many(multiple)
#morph-->shape
""" 
ekhane amra make_sound()diye sobgula kei se access korte parteche and 
various animal er jonno various sound korteche ....ekhane bujha jacche j
ei make_sound() er onekgula shape ache jetake amra boli polymorphism ...
"""


class Animal:
    def __init__(self,name) -> None:
        self.name=name 

    def make_sound(self):
        print('Animal making some sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Meow, meow')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('gheue gheue')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('bey, vey')

don=Cat('Real don')
don.make_sound()

shepard=Dog('Local shepard')
shepard.make_sound()

mess=Goat('Lo - Me')
mess.make_sound()

less=Goat('gora gori')

animals=[don,shepard,mess,less]
for animal in animals:
    animal.make_sound()