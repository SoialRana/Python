
class Calcultor:
    brand='casio'

    def add(self,num1,num2):
        res1=num1+num2
        return res1
    
    def subtract(self,num1,num2):
        res2=num1-num2
        return res2
    
my_cal=Calcultor()
result=my_cal.add(34,23)
result2=my_cal.subtract(34,23)
print(result)
print(result2) 
