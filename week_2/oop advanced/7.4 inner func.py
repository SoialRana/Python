# function is a first class object

def double_decker():
    print('starting the double decker')
    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun # fun er vitore fun call 
#print(double_decker()) # ekhane functon ta return korbe 
# print(double_decker()()) # ekhane result ta pabo 

def do_something(work):
    print('Work started')
    #print(work)
    work()
    print('work ended') # function er vitore amra chaile ekta parameter pathate pari

# do_something(2)
# do_something('i am busy')

def coding():
    print('coding in python')

do_something(coding)

def sleeping():
    print('sleeping and dreaming in python')

# do_something(sleeping)