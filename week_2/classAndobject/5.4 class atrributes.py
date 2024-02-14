class Shop:
    cart=[] # cart is a class attribute
    # amra jodi method er vitore declare na kori taile setake bola hoi class attribute
# class attribute sobgula instance er sathe share hoi se jonno rahim er 
# value gulo nipu er jonno again add hoye geche 
    def __init__(self,buyer):
        self.buyer=buyer

    def add_to_cart(self,item): # amra add_to_cart name ekta method nichi sekhane self thakbe bydefault
        self.cart.append(item)
        # amader jodi kono property or attribute k access korte hoi taile self. use korte hoi 
    # ekhane add_to_cart hocche method
rahim=Shop('Shuvo')
rahim.add_to_cart('shoes')
rahim.add_to_cart('phone')
print(rahim.cart)

nipu=Shop('Nipu')
nipu.add_to_cart('cycle')
nipu.add_to_cart('bycycle')
print(nipu.cart) # amara nipu er cart take access korte cacche 
# class attribute add korar somoy kheyal rakhte hobe eta ki instance er sathe meal thakbe naki onno kisur sathe meal thakbe

 