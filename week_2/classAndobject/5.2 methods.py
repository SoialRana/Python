def call():
    print('Calling someone i dont know')
    return 'call done'

class Phone:
    price=23433
    color='blue'
    brand='samsung' #ei features gulo dynamic na
    features=['camera','speaker','hammer']

    def call(self):# jehetu function er vitore tai self use korchi
        print('calling one person')

    def send_sms(self,phone,sms): # first parameter self hisebe count korbe,then baki jei parameter gulo pathabo segula dite hobe 
        #ekhane first parameter ta instance or self hisebe dhore nibe 
        text=f'sending sms to:{phone} and message:{sms}'
        return text

my_phone= Phone()
print(my_phone.features) # features 3 ta show korbe
my_phone.call() #python e class er vitore kawke call korbe parameter hisebe self pathate hoi 
result= my_phone.send_sms(23453,'i missed yyyou')
print(result)

# by default class vitore function add korle sekhetre extra parameter hisebe self dite hobe 



# home work add,sub,mul and div
class Calculator:
    brand='casio ms990'# attribute
    def add(self,num1,num2):
        pass

    #deduct method

    #multiply method

    #divide method