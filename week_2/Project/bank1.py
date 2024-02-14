class Bank:
    def __init__(self):
        self.accounts = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature = True

    def create_account(self, account_number, account_holder):
        account = Account(account_number, account_holder)
        self.accounts.append(account)
        print(f"Account created successfully. Account Number: {account_number}")

    def check_total_balance(self):
        print(f"Total Available Balance in the Bank: {self.total_balance}")

    def check_total_loan_amount(self):
        print(f"Total Loan Amount in the Bank: {self.total_loan_amount}")

    def toggle_loan_feature(self):
        self.loan_feature = not self.loan_feature
        status = "ON" if self.loan_feature else "OFF"
        print(f"Loan Feature is now {status}")

    def bankrupt(self):
        for account in self.accounts:
            account.withdraw(account.balance)
        print("The bank is bankrupt!")


class Account:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0
        self.loan_limit = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: +{amount}")
        print(f"Amount {amount} deposited successfully. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: -{amount}")
            print(f"Amount {amount} withdrawn successfully. New balance: {self.balance}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def transfer_amount(self, recipient_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transfer: -{amount} to Account Number {recipient_account.account_number}")
            recipient_account.transaction_history.append(f"Transfer: +{amount} from Account Number {self.account_number}")
            print(f"Amount {amount} transferred successfully to Account Number {recipient_account.account_number}")
            print(f"Sender's new balance: {self.balance}, Recipient's new balance: {recipient_account.balance}")
        else:
            print("Insufficient balance!")

    def take_loan(self):
        if Bank.loan_feature:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            self.loan_limit += loan_amount
            self.transaction_history.append(f"Loan: +{loan_amount}")
            print(f"Loan amount of {loan_amount} granted successfully.")
            print(f"New balance: {self.balance}, Loan Limit: {self.loan_limit}")
        else:
            print("Loan feature is currently turned off by the bank.")

    def check_transaction_history(self):
        print(f"Transaction History for Account Number {self.account_number}:")
        for transaction in self.transaction_history:
            print(transaction)


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, account_number, account_holder):
        self.bank.create_account(account_number, account_holder)

    def check_total_balance(self):
        self.bank.check_total_balance()

    def check_total_loan_amount(self):
        self.bank.check_total_loan_amount()

    def toggle_loan_feature(self):
        self.bank.toggle_loan_feature()


# Usage example
bank = Bank()

admin = Admin(bank)

# Create accounts
admin.create_account("123456789", "John Doe")
admin.create_account("987654321", "Jane Smith")

# Deposit and Withdrawal
account1 = bank.accounts[0]
account1.deposit(500)
account1.withdraw(200)

# Transfer Amount
account2 = bank.accounts[1]
account1.transfer_amount(account2, 300)

# Check Balance
account1.check_balance()

# Take Loan
account1.take_loan()

# Transaction History
account1.check_transaction_history()

# Admin Actions
admin.check_total_balance()
admin.check_total_loan_amount()
admin.toggle_loan_feature()

# Bankruptcy
bank.bankrupt()
