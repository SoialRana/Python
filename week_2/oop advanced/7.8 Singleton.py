# singleton--> one single instance
# if you want a new instance, you wil get the old one(already created)instance

class Singleton:
    __instance=None
    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance=self # current instance na thakle self k niye nibe
        else: # jodi instance thake 
            raise Exception('This is Singleton.Alreay have and instance,use that one by one calling get_instace method')

    @staticmethod 
    def get_instance():
        if Singleton.__instance is None:
            Singleton() #jodi instance take nite chay jodi instance na thake taile singleton()class k call korbe otherwise instance k call korbe 
        return Singleton.__instance
    
first=Singleton.get_instance()
second=Singleton.get_instance()
third= Singleton.get_instance() #ssecond or third bar same store dekhabe 
print(first)
print(second)
print(third)

#last=Singleton() # eta abar call dile ekta exception error dibe ... 

# eta ekbar call dile seta bar bar use korte hobe ...bar bar call dite parbo na 
""" UML -> Unified modeling language ...eta niye ektu porte hobe tader nijossho website 
 """