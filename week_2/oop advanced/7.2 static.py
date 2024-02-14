# static attribute (class attribute same as static attribute)
# static methos @staticmethod
# class method @classmethod
# difference between static method and class method 


class Shopping:
    cart=[] #class attribute  # static attribute
    orgin='china'

    def __init__(self,name,location) -> None:
        # init er vitore kisu likhle seta hobe instance attribute 
        self.name=name # instance attribute
        self.location=location

    def purchase(self,item,price,amount):
        remaining=amount-price
        price(f'buying: {item} for price: {price} and remaining : {remaining}')

    @staticmethod  # @ eta hocche decorator 
    def multiply(a,b):
       # print(self.name)  #.... static method e instance er kisu use kora jabe na
        result= a*b
        print(result)

    @classmethod
    # amra jehetu bole dichi j eta hocche classmethod tie result show korbe 
    def hudai_dekhi(self,item):
        # print(self.name) .... ekhane amra self parameter hisebe dichie 
        print('hudai dekhi kintu kinmu just ac er kawa khaite aschi',item)


        
baundhara=Shopping('basu en dhara', 'not popular location')
# baundhara.purchase('lungi',500,1000)# ekhane ami instance er upor use kortechi ar niche class er upoor 



# baundhara.hudai_dekhi('lungi')
#Shopping.purchase(2,3,3) # ekhetre 4 ta argument dite hobe otherwise result error show korbe ...missing 1 required positional argument 
#....class diye jokhon amra access korte jabo tokhon ekta extra property self soho chay 

Shopping.hudai_dekhi('Lungi') # class method ..amara ekhane instance er upor chalate parbo karon upore amra ble dichi eta class method 

Shopping.multiply(4,6) # static method .... static method jokhon amra use korbo tokhon amra self er value diboi na 
baundhara.multiply(4,2)


# static method k amra instance chara use korte pari but class method k use korte chaile instance chara use korte parbo na  