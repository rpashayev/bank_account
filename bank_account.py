class BankAccount: # creating BankAccount class
    
    all_accounts = [] # list to keep all accounts (instances / objects of BankAccount class)
    
    def __init__(self, int_rate, balance = 0): # BankAccount class constructor. 2 parameters: interest rate(int_rate) and balance. We set defaul value for balance equal to 0
        self.int_rate = int_rate #assigning parameter to instance. left part can be anything (f.ex self.interest_rate = int_rate), but right side must be parameter variable
        self.balance = balance
        BankAccount.all_accounts.append(self) # this code adds bank account (instance of BankAccount class) to the list from row 3
        
    def deposit(self, amount): # method of BankAccount class to add money to the account
        self.balance += amount # incrementing (+= which is self.balance = self.balance+amount) the balance of the account by the amount specified
        return self # returns updated instance (object)
        
    def withdraw(self, amount): # method of BankAccount class to add withdraw from the account
        if(self.balance >= amount): # checking if the account has sufficient balance
            self.balance -= amount # withdraw (decrease balance by the amount specified) from account
        else: # if balance less than amount decrease balance by $5
            print(f'Insufficient funds of account {BankAccount.all_accounts.index(self)+1}: Charging a $5 fee')
            self.balance -= 5 
        return self # returns updated instance (object)
    
    def display_account_info(self): # simply prints account info
        print(f'Account {BankAccount.all_accounts.index(self)+1} balance: ${self.balance}')
        
    def yield_interest(self):
        if(self.balance > 0):
            self.balance *= (1 - self.int_rate)
        return self
    
    @classmethod #that is class method (function) decoration. Meaning that we have to invoke/call it only for class (NOT instance)
    def print_all_statements(cls): # printing all statements
        i = 0
        for account in cls.all_accounts:
            print(f'Account {i} balance is ${account.balance}')
            i +=1
# ba1 is an instance (object) of our BankAccount class. Basically, it's new account we create with 1% interest rate and 500 initial balance. That is how we build our constructor on row 5. NOTE: to create an instance we give it a name(variable, ba1 in this case) and make it equal to class name with parameters from our constructor
ba1 = BankAccount(0.01, 500)

#here we invoke methods (functions) of our class. The structure is: instance (variable to which we assigned class at row 37), then dot followed by method name with arguments (REMEMBER: parameters - when we create method/function, argument - when we pass real data invoking the method/function)
ba1.deposit(200).deposit(100).deposit(250).withdraw(400).yield_interest().display_account_info()

#same comment as row 36 - we create 2nd account 
ba2 = BankAccount(0.01, 150)
ba2.deposit(800).deposit(125).withdraw(400).withdraw(111).withdraw(22).withdraw(100).yield_interest().display_account_info()

#same comment as row 36 - we create 3rd account
ba3 = BankAccount(0.05)
ba3.withdraw(1450).yield_interest().deposit(5).display_account_info()

# here we invoke / call class's method from row 31. Therefore, we first put class name (BankAccount), then do, followed by method
BankAccount.print_all_statements()

