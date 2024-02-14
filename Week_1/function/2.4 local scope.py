# global variable 
balance=2222
def buy_things(item,price):
    #balance=600
    # local scope variable 
    
    # you can access global variable without using the global keyword
    global balance # global balance k use korte chaile amra global keyword ta use korbo
    
    # if you want to modify a global variale , you have to use the global keyyword
    print('Previous balance value:',balance)
    balance-=price
    print(f'balance after buying : {item}' ,balance)


buy_things('sunglass' , 1000)
print('Global balance after buy', balance) 


# python er function er vitorer variable hocche local variable 
# local variable use korte chaile local variable k fun er vitore sobar upore rakhte hobe 
# amra global variable k func er vitore use korte parbo kintu jodi amra global value k modify 
# korte chay then global keyword use korte hobe otherwise global balnce k modify korte parbo na 