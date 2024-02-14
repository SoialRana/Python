# jodi amra 3 ta argument pathay kintu amra parameter hisebe 2 ta receive kori taile error dekhabe 
# abar jodi amra argument 2 ta pathay but parameter 3 ta receive kori taileo result error dekhabe 
# ei problem ta solve korar jonno amra jodi argument beshi pathay taile parameter er jaigay 0 dibo (num3=0)
# jodi amra num3 ta pathay taile value receive kore jog korbe otherwise num3=0 eta kaj korbe 

def sum(num1,num2,num3=0,num4=0,num5=0):#amra default hisebe j koita dekhte chay segula parameter hisebe pathay dibo
    result=num1+num2+num3+num4+num5
    return result
total=sum(99,11,6)
print('Total: ',total)



# jodi amra na jani j koita number add korbo taile amra *numbers korlei hobe ekhetre thik output asbe

""" #args
def all_sum(num1,num2,*numbers):
    print(numbers)

total=all_sum(45,46,34,65) # egulake se tuple er moto print korbe 
print('All sum is= ',total) """


#args
def all_sum(num1,num2,*numbers): # ei line e num1,num2 dewa mane num1,num2 chara baki gulo print korbe 
    # ekhane first 2 ta number se num1,num2 er moddhe rakhbe but baki value gulo se numbers er moddhe rakhbe 
    # tie jog korar somoy sudhu sesher 4 ta value jog korbe 
    print(numbers)# first 2 ta number show korbe na
    sum=0
    # ekhane amra hoi kono kisu patahbo na otherwise 1 ta pathate parbo na ...hoi 2 er odhik pathabo or kono value 
    # pathabo na otherwise wrong dekhabe
    for num in numbers:
        print(num)
        sum=sum+num
    return sum # for loop er vitore return kora jabe na

total=all_sum(45,46,34,65,34,5)
print('All sum is= ',total)
# egulake lokjon *numbers na bole *args bole 

def do_a_lot(*args):# *args bola mane amra 0 theke many sonkhok parameter pathate pari
    print(args) # jei args or number gulo pathailam segula  print korbo