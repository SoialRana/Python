""" highest=max([34,23,54,343])
smallest=min([34,23,54,343])
count=len([2,4,5,6])
total=sum([23,34,45,56,76,45])
print(highest, smallest,count,total)

 """

# onno kono file theke jodi amra kono fun import korte chay taile evabe korte pari

from function import * #jodi amra sobgula function import korte chay 
from function import double_it as dt
from kargs_multiple import full_name as name
# full_name ta k jodi amra choto name dite chay taile as diye name tar nam likhte hobe 
f_name= name('tomato' , 'alu')
print(f_name)

# result=double_it(45)
result=dt(45)
print(result)