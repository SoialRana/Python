class Vehicle:
    def __init__(self,name,price) -> None:
        self.name=name
        self.price=price
        
    def move(self):
        pass
    
    def __repr__(self) -> str:
        return f'{self.name} {self.price}'

class Bus(Vehicle):# bus vehicle theke inherit korbe 
    def __init__(self, name, price,seat) -> None:
        self.seat=seat
        super().__init__(name, price)# super e jegula parent theke asbe segula thakbe 

    def __repr__(self) -> str:
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price,weight) -> None:
        self.wieght=weight
        super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)
        # ekhane pickupTruck , Truck k inherit korche sekhan theke se weight ta pabe ,,abar truck
        # vehicle k inherit korche sekhan theke se name and price ta pabe ...tie tar jonno kisu lekha laglo na 

class ACBus(Bus): # jodi amra init kori taile name,price,seat automatic pabo...baki jegula pabo na segula ekhane likhe dibo
    def __init__(self, name, price, seat,temperature) -> None:
        self.temperature=temperature
        super().__init__(name, price, seat)

    def __repr__(self) -> str:
        print(f'{self.seat}')
        return super().__repr__()

green_line=ACBus('green', 234543423,22,32)
print(green_line)
# ekhane ac_bus k call korle se print korche seat ,,abar se j inherit korche bus k and bus inherit korche 
# vehicle k ..ekhane abar vehicle print korbe name and price ...so overall print hobe name,price and seat  
# tobe age child class er print hobe then base class ...so seat age print hobe 