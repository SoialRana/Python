from Menu import Pizza,Burger,Drinks,Menu
from Restaurant import Restaurant
from Users import Chef,Customer,Server,Manager
from order import Order

def main():
    menu=Menu()
    pizza_1=Pizza('Shutki Pizza',600,'large',['shutki','onion'])
    menu.add_menu_item('pizza',pizza_1)
    pizza_2=Pizza('Alur vorta pizza',300,'large',['potato','onion','oil'])
    menu.add_menu_item('pizza',pizza_2)
    pizza_3=Pizza('Dal Pizza',500,'large',['dal','oil'])
    menu.add_menu_item('pizza',pizza_3)

    #add burger to the menu
    burger_1=Burger('Naga Burger',1000,'chicken',['bread','chilli'])
    menu.add_menu_item('burger',burger_1)
    burger_2=Burger('Beef Burger',1200,'beef',['goruu','haddi'])
    menu.add_menu_item('burger',burger_2)

    # add drinks to the menu 
    coke=Drinks('coke', 50, True)
    menu.add_menu_item('drinks',coke)
    coffee=Drinks('Mocha',300,False)
    menu.add_menu_item('drinks',coffee)

    # show menu
    menu.show_menu()

    restaurant=Restaurant('Sai Baba Resturants',2000,menu)
    manager=Manager('Kala chan Manager',5,'kala@chan.com','kalipur',1500,'janu 1 2020','core')
    restaurant.add_employee('manager',manager)
    chef=Chef('Rustam',34,'rustom@ali.com','gitalgoch',2343,'feb 3 2022','chef','everythiing')
    restaurant.add_employee('chef',chef)
    server=Server('chotu server',34,'rahim@jai.com','din',3443,'March 1 2022','server')
    restaurant.add_employee('server',server)

    # show employees
    restaurant.show_employees()


    # customer
    customer_1=Customer('shuvo',455,'king@khan.com','gitl',34)
    order_1=Order(customer_1,[pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)

    # customer one paying for order_1
    restaurant.receive_payment(order_1,2000,customer_1)

    print('revenue and balance after first customer',restaurant.revenue,restaurant.balance)

     # customer2
    customer_2=Customer('rana',345,'king@sdf.com','goch',34)
    order_2=Order(customer_2,[pizza_1,burger_2,coffee])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)

    # customer one paying for order_1
    restaurant.receive_payment(order_2,2000,customer_2)

    print('revenue and balance after second customer',restaurant.revenue,restaurant.balance)


    #pay rent
    restaurant.pay_expense(restaurant.rent,'Rent')
    print('After rent',restaurant.revenue,restaurant.balance,restaurant.expense)

    restaurant.pay_salary(chef)
    print('After salary',restaurant.revenue,restaurant.balance,restaurant.expense)

# call the main 
if __name__=='__main__':
    main()