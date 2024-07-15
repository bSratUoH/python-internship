class BankAccount:
    def _init_(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount should be greater than zero.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.balance}.")
        else:
            print("Withdrawal amount should be greater than zero and less than or equal to balance.")
    
    def get_balance(self):
        return self.balance


account1 = BankAccount("123456789", "Alice")
print(f"Initial balance: ${account1.get_balance()}")

account1.deposit(1000)
account1.withdraw(400)
account1.withdraw(800)  # This withdrawal will fail due to insufficient funds
print(f"Final balance: ${account1.get_balance()}")

