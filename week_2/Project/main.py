# from bank import Bank,Account
class Bank:
    def __init__(self,name) -> None:
        self.name=name
        self.accounts=[]
        self.loan_features=True


    def add_account(self,account):
        self.accounts.append(account)
        print(f'Added account {account} is successfully in the bank')


    def remove_account(self,account):
        self.accounts.remove(account)
        print(f'Remove account:{account} successfully in the bank')


    def toggle_loan_features(self):
        self.loan_features=not self.loan_features
        status='ON' if self.loan_features else 'OFF'
        print(f'loan features is now {status}')


class Account:
    def __init__(self,account_number,owner,balance=0) -> None:
        self.account_number=account_number
        self.owner=owner
        self.balance=balance
        self.transactions=[]
        self.loan_limit=0


    def deposit(self,amount):
        self.balance+=amount
        self.transactions.append(Transaction(amount,'Deposit'))
        #print(f'Amount {amount} deposited succesfully.New balance:{self.balance} account number {self.account_no}')


    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            self.transactions.append(Transaction(amount,'Withdraw'))
            #print(f'amount {amount} withdrawn successfully.New balance:{self.balance} account number : {self.account_no}')
        else:
            print('Insufficient balance!')


    def check_balance(self):
        print(f'Available balance: {self.balance}')


    def transfer_amount(self,recipient_acc,amount):
        if self.balance>=amount:
            self.balance-=amount
            recipient_acc+=amount
            self.transactions.append(Transaction(amount,'Transfer amount'))
            print(f'Amount {amount} transferred successfully to account number {recipient_acc}')
        else:
            print('Insufficient balance')

    
    def take_loan(self):
        if Bank.loan_features:
            loan_amount=self.balance*2
            self.balance+=loan_amount
            self.loan_limit+=loan_amount
            self.transactions.append(Transaction(loan_amount,'loan'))
            print(f'Loan amount of {loan_amount} granted successfully')
        else:
            print('Loan feature is turned off')



class Transaction:
    def __init__(self,amount,type) -> None:
        self.amount=amount
        self.type=type



def main():
    bank_name=input('Enter bank name: ')
    bank=Bank(bank_name)
    print('Bank', bank_name, 'Created Succesfully')
    while True:
        print('1. Create Account')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        choice=int(input('Enter your choice: '))
        if choice==1:
            acc_number=input('Enter account number: ')
            acc_owner=input('Enter account owner name: ')
            acc_balance = float(input('Enter opening balance: '))
            account=Account(acc_number,acc_owner,acc_balance,)
            bank.add_account(account)
            print('Account created succesfully..')

        elif choice==2:
            acc_number=input('Enter account number:')
            amount=float(input('Enter amount to deposit: '))
            account=find_account(bank.accounts,acc_number)
            if account:
                account.deposit(amount)
                print('Deposit successfully')
            else:
                print('Account not found')

        elif choice==3:
            acc_number=input('Enter a account number: ')
            amount=float(input('Enter a amount to withdraw: '))
            account=find_account(bank.accounts,acc_number)
            if account:
                account.withdraw(amount)
                print('Withdraw successfully')
            else:
                print('Account not found ')

        elif choice==4:
            print('Thank you for using bank management system')
            break
        else:
            print('Invalid choice')


def find_account(accounts,number):
    for account in accounts:
        if account.number==number:
            return account
        
if __name__=='__main__':
    main()