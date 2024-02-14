class Person:
    id_counter=100
    def __init__(self,email,password) -> None:
        self.email=email
        self.password=password
        """ self.user_id=Person.id_counter
        Person.id_counter+=1 """
        self.user_id=Person.generate_id()


    @classmethod
    def generate_id(self):
        id=self.id_counter
        self.id_counter+=1
        return id


    def __repr__(self) -> str: # ekta object k kivabe represent korte hoi seta korte pari
        return f'Email :{self.email} and password: {self.password} person_id={self.user_id}' 


class Product:
    def __init__(self,name,price,quantity) -> None:
        self.name=name
        self.price=price
        self.quantity=quantity

    def __repr__(self) -> str:
        return f'Product name: {self.name}|| Product price: {self.price}|| Product quantity: {self.quantity}'



class Store: 
    def __init__(self) -> None:
        self.total_products={} # ekahne dictionary use korchi karon dictionary 
                   # diye sob seller er sob product access korte parbo 

    def add_product(self,seller_id,product):
        #print(seller_id)
        productDict=vars(product) # product gulo k dictionary te convert kore vars
        #print(productDict)
        if seller_id not in self.total_products:
            self.total_products[seller_id]=[]

            seller_info={}
            seller_info["total_sell_product"]=0
            seller_info["total_sell_amount"]=0
            seller_info["total_profit_amount"]=0
            self.total_products[seller_id].append(seller_info)
        self.total_products[seller_id].append(productDict)



class Owner(Person):
    def __init__(self, email, password) -> None:
        self.total_sell_products=0
        self.total_sell_amount=0
        self.total_profit_amount=0
        super().__init__(email, password)



class Seller(Person):
    def __init__(self, email, password) -> None:
        super().__init__(email, password)


    def add_product(self,store,product_name,product_price,product_quality):
        product=Product(product_name,product_price,product_quality)
        #print(product)
        store.add_product(self.user_id,product)


    def sell_info(self,store):
        #print(self.user_id)
        print(store.total_products[self.user_id])




class Customer(Person):
    def __init__(self, email, password) -> None:
        self.total_buy_amount=0
        self.total_buy_products=0
        super().__init__(email, password)


    def show_product(self,store):
        all_seller_key=store.total_products.keys()
        #print(all_seller_key)
        for seller_id in all_seller_key:
            print('Seller id :',seller_id)
            print('==================')
            #for product in store.total_products[seller_id]:
            for index in range(1, len(store.total_products[seller_id])):
                product=store.total_products[seller_id][index]
                print("name: ",product["name"], "price: ",product["price"], "quantity: ", product["quantity"])


    def buy_product(self,store,seller_id,product_name,quantity):
        #print(store.total.products)
        #print(store.total_products[seller_id])
        for index in range(1,len(store.total_products[seller_id])):
            product=store.total_products[seller_id][index]
            #print(product)
            if product["name"]==product_name:
                #print(product)
                product["quantity"]-=quantity
                self.total_buy_products+=quantity
                self.total_buy_amount+=product["price"]*quantity
                seller=store.total_products[seller_id][0]
                seller["total_sell_product"]+=quantity
                seller["total_sell_amount"]+=product["price"]*quantity
 
store=Store()

seller1=Seller("seller1@gmail.com",12345)
seller2=Seller("seller2@gmail.com",54321)
seller3=Seller("seller3@gmail.com",54321)
# print(seller1)
# print(seller2)
# print(seller3)

seller1.add_product(store,'iphone10',110,12)
seller1.add_product(store,'iphone11',1104,11)

seller2.add_product(store,'samsung_j7',1120,14)
seller2.add_product(store,'samsung_A30s',3110,15)

seller3.add_product(store,'Oppo',1102,16)
seller3.add_product(store,'Oppo1',1101,17)


customer1=Customer('customer1@gmail.com',12345)
#customer1.show_product(store)
# print(store.total_products)
#print(customer1.total_buy_products,customer1.total_buy_amount)
customer1.buy_product(store,100,'iphone10',5)

print()
print()
#customer1.show_product(store)
# print(store.total_products)

#print(customer1.total_buy_products,customer1.total_buy_amount)

# seller1.sell_info(store)
# seller2.sell_info(store)

customer1.buy_product(store,101,'samsung_j7',11)
# print()
# print()
# seller1.sell_info(store)
# seller2.sell_info(store)
print(store.total_products)

owner=Owner('admin@gmail.com',1234)
