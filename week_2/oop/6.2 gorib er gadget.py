
class Laptop:
    def __init__(self,brand,price,color,memory) -> None:
        self.brand=brand
        self.price=price
        self.color=color # jei color ta parameter asbe seta receive korbe
        self.memory=memory
    def run(self): # user define function
        return f'Running Laptop: {self.brand}'
    
    def coding(self):
        return f'Learning python and practicing'
    
class phone:
    def __init__(self,brand,price,color,dual_sim) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.dual_sim=dual_sim

    def run(self):
        return f'phone tipa tipi kore din sesh'
    
    def phone_call(self,number,text):
        return f'Sending SMS to: {number} with:{text}'

""" Amra ekhane dekhte pai laptop class and phone class er moddhe kisu property common ..as brand,price
    price,and color ei property gulo same   ....abar both class e run method ta ache common ...ekhane kisu 
    uncommon functionality ache as laptop er khetre memory and coding method  and phone er khetre dual_sim 
    and phono call method .. 
    ei same jinish gulo amra jate bar bar na likhi er jonno amader ekta jinish jante hoi seta holo inheritance 
"""


class Camera:
    def __init__(self,brand,price,color,pixel) -> None:
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel

    def run(self):
        pass
    def change_lens(self):
        pass