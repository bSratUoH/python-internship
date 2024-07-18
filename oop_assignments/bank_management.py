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


# account1 = BankAccount("123456789", "Alice")
# print(f"Initial balance: ${account1.get_balance()}")

# account1.deposit(1000)
# account1.withdraw(400)
# account1.withdraw(800)  # This withdrawal will fail due to insufficient funds
# print(f"Final balance: ${account1.get_balance()}")
# # hjfkd


def division(a, b):
    try:
        return a // b
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    except TypeError:
        return "Only numbers are allowed."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


import unittest

class TestStringMethods(unittest.TestCase):
    def test_division(self):
        res = division(10, 2)
        self.assertEqual(res, 5)

        res1 = division(10, 0)
        self.assertEqual(res1, "Division by zero is not allowed.")
        
        self.assertEqual(division("10", 2), "Only numbers are allowed.")
        self.assertEqual(division(10, "2"), "Only numbers are allowed.")
        self.assertEqual(division("10", "2"), "Only numbers are allowed.")
        # self.assertEqual(division(10, 2, 3), "An unexpected error occurred: division() takes 2 positional arguments but 3 were given")



unittest.main()      

