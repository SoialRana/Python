""" 
def sum(num1,num2,num3=0,num4=0,num5=0):#amra default hisebe j koita dekhte chay segula parameter hisebe pathay dibo
def function_name(num1,num2,*args, **kargs): amra chaile normal parameter(num1,num2) pathate pare...abar chaile arg hisebe
pathate pari ....abar chaile key wala argument hisebe parameter pathate pari 
"""




def full_name(first, last):
    name=f'Full name is: {first} {last}'
    #name=first+' '+last  # evabe declare kora jabe string ta 
    # amra dynamic vabe first and last k bosalam
    return name

# take parameters in oreder (serial wise)
# name=full_name('alu','peyaj')
name=full_name(last='peyaj',first='kodu')
# jodi amra last ta age print korte chay serial wise print korte na chay
print(name)

# define famous (**key args...kargs)
def famous_name(first,last, **addition): #**addition first and last bad diye baki parameter gulo key wala arguments addition er moddhe rakhbo
    
    name=f'{first} {last}'
    #print(addition['title'])
    for key, value in addition.items():
        print(key,value)
        # ekhane protekk key and value k print korbe jekhane key hocche (first,last,title)and value hocche {taher,ali,hujur}
        #key wala argument er khetre first e key then value print hobe 
    return name

name =famous_name(first='Taher', last='ALi',title="hujur",title2="shayokh",
                  last2='taheri')
print(name)


#def function_name(num1,num2,*args, **kargs):


# fun er khetre ekadhik value return korar proces 
def a_lot(num1,num2):
    sum=num1+num2
    mul=num1*num2
    rem=num1-num2
    # return [sum,mul,rem] # jodi amra list arare return kori taile list return korbe otherwise
    return sum,mul,rem  # tuple hisebe return korbe

everything=a_lot(33,22)
print(everything)