class Bank:
    def __init__(self,name) -> None:
        self.name=name
        self.accounts=[]
        self.check_balance=0
        self.total_loan_amount=0
        self.loan_feature=True

    def create_account(self,account_number,owner):
        account=Account(account_number,owner)
        self.accounts.append(account)
        print(f'Added account {account_number} is successfully in the bank')


    def remove_account(self,account):
        self.accounts.remove(account)
        print(f'Remove account:{account} successfully in the bank')


    def check_balance(self):
        print(f'Available balance: {self.balance}')

    
    def total_loan_amount(self):
        print(f'Total loan amount in the bank: {self.total_loan_amount}')



    def toggle_loan_feature(self):
        self.loan_feature=not self.loan_feature
        status='ON' if self.loan_feature else 'OFF'
        print(f'loan features is now {status}')


    def bankrupt(self):
        for account in self.accounts:
            account.withdraw(account.balance)
        print('The bank is bankrupt')


class Account:
    def __init__(self,account_number,owner) -> None:
        self.account_number=account_number
        self.owner=owner
        self.balance=0
        self.transactions=[]
        self.loan_limit=0


    def deposit(self,amount):
        self.balance+=amount
        self.transactions.append(f'Deposit: +{amount}')
        print(f'Amount {amount} deposited succesfully.New balance:{self.balance} account number {self.account_number}')


    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            self.transactions.append(f'Withdraw: -{amount}')
            print(f'amount {amount} withdrawn successfully.New balance:{self.balance} account number : {self.account_number}')
        else:
            print('Insufficient balance!')



    def check_balance1(self):
        print(f'Available balance: {self.balance}')



    def transfer_amount(self,recipient_acc,amount):
        if self.balance>=amount:
            self.balance-=amount
            recipient_acc.balance += amount
            self.transactions.append(f'Transfer: +{amount} succesfully')
            print(f'Amount {amount} transferred successfully to account number {recipient_acc.account_number}')
        else:
            print('Insufficient balance')

    
    def take_loan(self):
        if Bank.loan_feature:
            loan_amount=self.balance*2
            self.balance+=loan_amount
            self.loan_limit+=loan_amount
            print('Transfer succesfully')
            print(f'Loan amount of {loan_amount} granted successfully')
        else:
            print('Loan feature is turned off')


    def transaction(self):
        print(f'----Transaction history are------')
        for transaction in self.transactions:
            print(transaction)



class Admin:
    def __init__(self,bank) -> None:
        self.bank=bank

    def create_account(self,account_number,owner):
        self.bank.create_account(account_number,owner)

    def check_balance(self):
        self.bank.check_balance()

    def total_loan_amount(self):
        self.bank.total_loan_amount()

    def toggle_loan_feature(self):
        self.bank.toggle_loan_feature()



bank=Bank('My bank')
admin=Admin(bank)

admin.create_account('11111','Rahim')
admin.create_account('22222','Karim')

account1=bank.accounts[0]
account1.deposit(5000)
account1.withdraw(300)

account1.check_balance1()


account2=bank.accounts[1]
account2.deposit(5000)
account2.withdraw(3500)

account2.check_balance1()


# Transfer Amount
account1.transfer_amount(account2, 300)

# Check Balance
account1.check_balance1()
account2.check_balance1()


# Take Loan
#account1.take_loan()

# Transaction History
account1.transaction()
