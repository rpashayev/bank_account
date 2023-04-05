class BankAccount:
    
    all_accounts = []
    
    def __init__(self, int_rate, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        if(self.balance >= amount):
            self.balance -= amount
        else:
            print(f'Insufficient funds of account {BankAccount.all_accounts.index(self)+1}: Charging a $5 fee')
            self.balance -= 5
        return self
    
    def display_account_info(self):
        print(f'Account {BankAccount.all_accounts.index(self)+1} balance: ${self.balance}')
        
    def yield_interest(self):
        if(self.balance > 0):
            self.balance *= (1 - self.int_rate)
        return self
    
    @classmethod
    def print_all_statements(cls):
        for account in cls.all_accounts:
            print(account)

ba1 = BankAccount(0.1, 500)
ba1.deposit(200).deposit(100).deposit(250).withdraw(400).yield_interest().display_account_info()

ba2 = BankAccount(0.01, 150)
ba2.deposit(800).deposit(125).withdraw(400).withdraw(111).withdraw(22).withdraw(100).yield_interest().display_account_info()

ba3 = BankAccount(0.05)
ba3.withdraw(1450).yield_interest().deposit(5).display_account_info()

BankAccount.print_all_statements()

