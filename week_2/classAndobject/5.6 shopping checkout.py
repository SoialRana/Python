class Shopping:
    def __init__(self,name):
        self.name=name
        self.cart=[] # empty instance attribute 

    def add_to_cart(self,item,price,quantity):
        product={'item':item, 'price': price, 'quantity':quantity}
        self.cart.append(product)
    
    #def remove_item(self,item):

    def checkout(self,amount):# jinish gulor jonno amake taka dite hobe 
        total=0
        for item in self.cart:
            #print(item) 
            # ekahne item gulo ekta dictionary er moddhe ache kintu overall sobgula item 
            # ekta list er moddhe ache tie amader nicher for loop ta chailaite hobe 
            total+=item['price'] * item['quantity']
        print('total price',total)
        if amount<total:
            print(f'please provide {total-amount} more')
        else:
            extra= amount-total
            print(f'Here is your items and extra money:{extra}') 

shuvo=Shopping('Arafat hossain')
shuvo.add_to_cart('Alu',34,5)
shuvo.add_to_cart('dim',40,3)
shuvo.add_to_cart('rice',30,8)
print(shuvo.cart)
shuvo.checkout(600)