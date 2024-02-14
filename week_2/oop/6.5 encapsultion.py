# encapsultion-->hide details
# access_modifier= public,private ,protected...k koto tuku access korte pare

#ekhane amra balance ta kawke dekhte dite cacchi na etake capsule diye abritto kore rakhbo eta hocche encapsulation   
# amra implementation ta hide korte pari eta hocche encapsulation

class Bank:
    def __init__(self,holder_name,initial_deposit) -> None:
        self.holder_name=holder_name# public attribute
        self._branch='banani 11'# protected attribute
        self.__balance =initial_deposit # private ..amra balance ta kawke dekhte dibo na 
        # etake amra bahir theke access korte parbo na kintu take class er sobjaigay use korte parbo

    def deposit(self,amount):  
        self.__balance+=amount 

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance=self.__balance-amount 
            return amount
        else:
            return f'Fokira taka nie'


rafsan=Bank('Chooto bro',10000)

print(rafsan.holder_name)
rafsan.holder_name='boro vai' # holder name change korlam 
#rafsan.balance=0 
rafsan.deposit(40000)
print(rafsan.get_balance()) # jehetu rafsan er balance ta private tie take direct access korte parbo na kintu amra 
# function or method er moddome take access korte pari 
print(rafsan.holder_name)

print(rafsan._branch) # _branch eta hocche protected variable 

#print(dir(rafsan))

print(rafsan._Bank__balance) # balance ta evabe show korte pari amra 