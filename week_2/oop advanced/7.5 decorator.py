import math
from math import factorial
import time 

def timer(func):
    # def inner(n): # eta korleo kaj hobe 
    def inner(*args, **kwargs): # kintu amra normally eta beshi use kore thaki
        print('time stated')
        start=time.time()
        #print(func)
        func(*args,**kwargs)
        print('time ended')
        end=time.time()
        print(f'total time taken {end-start}')
    return inner
#timer()()
""" Timer takes 0 positional argument but 1 was given ...jodi amra *args,**kwargs na diye thaki  ...taile error dekhabe 
    niche j decorator (@timer) ta ache seta jodi amra na diye thaki uporer fun call hobe na ...decorator hocche ekta nested fun 
    timer fun er vitore amader call kore dite hobe func()k otherwise get factorial call hobe na 
 
"""
@timer 
def get_factorial(n):
    print('factorial starting')
    # result=math.factorial(n)
    result=factorial(n)
    print(f'factorial of {n} is: {result}')

get_factorial(n=12)  # ekhan theke age factorial func k call hobe ..timer er jonno erpor timer func e call hobe evabe print hobe 



# def get_factorial():
#     print('factorial starting')

# vejailla way to decorate 
#timer(get_factorial)()


