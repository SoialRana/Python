# define
def double_it(num):
    result=num*2
    print(result)
    return result # return kora mane jate onno kew eta diye kisu ekta korbe 
# ei function ta comment korle nicher final value ta kaj korbe na

double_it(8)
double_it(44)

def sum(num1,num2):
    result=num1+num2
    return result
total=sum(44,88)# first value ta first parameter hobe 
print('Total value: ',total)

final=double_it(total) # double it func kono kisu return na korle output none dekhabe
print('Final value: ',final)