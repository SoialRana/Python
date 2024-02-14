class Phone:
    manufactur= 'China' # attribute

# pass mane ami ekhane kisu likhtechi na ei jaiga ta khali 
    # constructor 
    def __init__(self,owner,brand,price):
        self.owner=owner  # owner er ekta value(man) dibo seta owner namer attribute er man hisebe set hobe
        self.brand=brand  
        self.price=price
             # name...value 
        # eta hocche python er khetre constructor 
        # self er hisebe protekkta object er alada alada man set hobe 
    """ 
    def __init__(self):
        pass
    eta holo empty constructor jemon ta amra c++ e kortam ... empty constructor jodi amra use 
    koreo thaki taile amader ekta self ditei hobe otherwise constructor kaj korbe na 
    
    amar uddhesho ami phone theke onek gula phn banabo and every phone er tar nijossho kisu feature thakbe 
    amar ekta phone er class ache sei phone er onek gula object banabo and segular kisu alada value thakbe 
    but structure same thakbe ...suppose ami ekhane owner ,brand,price k alada banabo tar jonno self er pore oigula 
    likhbo 
    """
        
    def send_sms(self,phone,sms):
        text= f'sending to: {phone}{sms}'
        print(text)

my_phone=Phone('kalam','samsung',34453)
# ekhane phone er jonno to kono parameter nie taile parameter keno dorkar hocche ... eta dorkar hocche karon amra j init
# or initialize ta dichi setar jonno parameter dorkar hocche 3 ta parameter ...tie 3 ta parameter pathay dite hoiche ekhane 
print(my_phone.owner,my_phone.brand,my_phone.price)
# ekhane myphone.owner,brand, egula hocche instance 

her_phone=Phone('rahima','tecno',34234)
print(her_phone.owner,her_phone.brand,her_phone.price)
# ekhane amra same class k call kortechi kintu call korar somoy amra tar init er moddhe j parameter gulo dicchi setar upor base kore se amader notun kore ekta instance dicche

dad_phone= Phone('abbu','Nokia',2222)
print(dad_phone.owner,dad_phone.brand,dad_phone.price)
# same property er name kintu co=instance er upor base kore change hocche 
# class korar subidha hocche ei j data ba ei j object gulo toiri hocche tader structure ta same
# thakteche

