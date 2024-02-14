class Shop:
    shopping_mail='jamuna'
    def __init__(self,buyer) :
        self.buyer=buyer
        self.cart=[] # cart is an instance attributes
# self diye ekhane ja kisu declare korbo sobkisu hocche instance attribute 
    def add_to_cart(self,item):
        self.cart.append(item)
        # jekono ekta attribute k amra jekono jaiga theke use korte pari ...jemon amra ekhane cart attribute k use korchi

nipu= Shop('Nipu')
nipu.add_to_cart('shoe')
nipu.add_to_cart('phone')
print(nipu.cart)

jony=Shop('Jony')
jony.add_to_cart('hat')
jony.add_to_cart('watch')
print(jony.cart)


# ager example e class attribute chilo ...ar class attribute sobgula instance er sathe share hoi 
# tie rahim er product gulo nipu er product er sathe add hoye geche 