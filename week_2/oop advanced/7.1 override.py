class Person:
    def __init__(self,name,age,height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight

    def eat(self):
        print('vat,mangso ,polao ,korma')

    def exercise(self):
        raise NotImplementedError


class Crickter(Person):
    def __init__(self, name, age, height, weight,team) -> None:
        self.team=team # se kon team e ache 
        super().__init__(name, age, height, weight)
        
    # override 
    def eat(self):
        print('Vegetables') # ekhane parent class er eat method k 
           # child class er eat method ta override kore felche

    def exercise(self):
        print('Gym e poisa diya hudai gham jhorai')# ekkhaneo override kora hoiche
        # override na korle ekhaneo error dekhaito ...

    # + sign operator overload korchi 
    def __add__(self,other):
        return self.age + other.age
    # ekhane se first crickter er age nibe then second cricketer er age niye 2 take add kore dibe 
    
    
    # * sign operator overload
    def __mul__(self,other):
        return self.weight*other.weight
    # len overload
    def __len__(self):
        return self.height # sakib er hight ta show korbe 
    
    #operator overload
    def __gt__(self,other):
        return self.age>other.age # k boro seta show korbe 

sakib=Crickter('Sakib',34,54,23,'BD')
mushi=Crickter('mushi',3,5,2,'BD')
# sakib.eat()
# sakib.exercise()


# plus sign overload
print(45 + 54)
print('subho'+ 'raju')
print([12,98]+[5,6,7,1,2]) # 2 ta list k ekta list e convert korbe 
print(sakib + mushi)
print(sakib * mushi)
print(len(sakib))
print(sakib>mushi)