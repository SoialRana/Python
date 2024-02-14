# base class, parent class, common attributes + functionality class
# derived class, child class, uncommon attributes + functionality class


""" common attributes + functionaly jegula ache segula thakbe parent or base class e  
    common gula ekta class e rekhe sekhan theke amra inherit korbo 
"""
class Gadget:# base class ..ekhane amra common functionality/method and attribute gulo rakhbo...uncommon gula amra rakhbo na 
    def __init__(self,brand,price,color,origin) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.origin=origin
    
    def run(self):
        return f'Running Laptop: {self.brand}'

class Laptop:
    def __init__(self,memory,ssd) -> None:
        self.memory=memory # amra ekhane common gula rakhbona ...ekhetre amader duplication kome geche 
        self.ssd=ssd
        
    def coding(self):
        return f'Learning python and practicing'
    
class phone(Gadget):# ekhane amra inherit korbo gadget er property gulo k 
    def __init__(self,brand,price,color,origin,dual_sim) -> None:
        self.dual_sim=dual_sim # amader brand,price,color sobgula amra parent theke pathay dibo super() er sahajje 
        super().__init__(brand,price,color,origin)
        # ekhane super()call na korle 'object has no attribute ' ei error ta dekhabe 
    
    def phone_call(self,number,text):
        return f'Sending SMS to: {number} with:{text}'
    def __repr__(self) -> str:
        return f'phone: {self.brand} {self.price} {self.dual_sim}' 
    # represent er moddhe amra jegula pass korbo segulay sudhu show korbe 

class Camera:
    def __init__(self,pixel) -> None:
        self.pixel=pixel

    def change_lens(self):
        pass

# inheritance
my_phone=phone('iphone',12324,'silver','china',True)
#my_phone.phone_call()
print(my_phone.brand)

print(my_phone)
