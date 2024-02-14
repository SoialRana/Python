# read only--> you can not set the value. value can not be changed
# getter---> get a value of a property. Most of the time , you will get the value of a private attributes
# setter->  set a value of a property through a method . most of the
  # time you will set the value of a private property. 

class User:
    def __init__(self,name,age,money) -> None:
        self._name=name
        self._age=age
        self.__money=money

    # getter without any setter is readonly attribute
    @property # decorator  # etake se method er moddhe rakhteche na etake decorator ta attribute e convert korche ...eta ekhon kaj korbe na
    def age(self):
        return self._age
    
    #getter without any setter is readonly attribute 
    @property
    def salary(self):
        return self.__money
    
    #setter-> 
    @salary.setter
    def salary(self,value):
        if value < 0:
            return 'salary cannot be negative'
        self.__money+=value

#samsul=User('copa',34,5434)
#print(samsul.__money) # ekhane se private property k use korte parbe na 

# samsul=User('copa',34,5434)
# print(samsul.age()) # decorator dewar joonno ekhon eta kaj korbe na ..karon ekhon eta method nie eta attribute hoye giyeche ..ekhon nicher print() use kore kaj korte parbo

# print(samsul.age)  #.. attribute er moto kore ekhon call korte hobe

samsul=User('copa',34,5434)
print(samsul.age)
#print(samsul.salary()) # evabe call korle hobe na
print(samsul.salary) # evabe call korte hobe


samsul.salary=4555
print(samsul.salary)


""" 
@ diye kono ekta jinish kono fun er upor likha thakle setake decorator bole 
"""