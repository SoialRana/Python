class Book:
    def __init__(self,name) -> None:
        self.name=name
        
    """ def read(self):
        pass """
    
    # jokhon amra bolbo j eta implement kortei hobe tokhon amra pass er jaigay raise use kore thaki 
    def read(self):
        raise NotImplementedError # ekhetre ekta error show korbe  
# abstract class er moddhe jodi ami ekta method er moddhe pass diye thaki taile kono problem nie ..kintu ami jodi raise diye thaki 
# taile amake must be child class e seta implement kortei hobe otherwise error dibe 
class Physics(Book):
    def __init__(self, name,lab) -> None:
        self.lab=lab
        super().__init__(name)
        
    def read(self):
        print("Reading physics vectore ")
        
topon= Physics('topon',True)
print(issubclass(Physics,Book))
print(isinstance(topon,Physics))
print(isinstance(topon,Book))

topon.read() # pass kora bolte se skip kore chole jabe kono care korbe na 

#subclass or instance check korar jonno 