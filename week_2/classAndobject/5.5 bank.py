class Bank:
    def __init__(self,balance): # bank kholar jonno balance amader lagbe
        self.balance=balance
        self.min_withdraw=100
        self.max_withdraw=100000
        # sobsomoy j instance attribute gula parameter pass korei banate hobe emonta na ..kisu nijossho parameter thakte pare
        # jemon ta ekhane 2 ta nijossho parameter banalam 

    def get_balance(self):
        return self.balance
    
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount

    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print(f'fakira you can withdraw below{self.min_withdraw}') 
        elif amount>self.max_withdraw:
            print(f'bank fakir hoye jabe. you can not with more than{self.max_withdraw}') 
        else:
            self.balance-=amount
            print(f'here is your money {amount}') 
            # print(f'your balance after withdraw{self.balance}')
            print(f'your balance after withdraw{self.get_balance()}')
            # amra chaile ekta method er vitore theke arekta method k call korte pari 
        
brac=Bank(15000)
brac.withdraw(34)
brac.withdraw(343344)
brac.withdraw(1000)


dbbl=Bank(5000)
dbbl.deposit(3000)
dbbl.deposit(2000)
print(dbbl.get_balance())