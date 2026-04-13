"""
File: checkingaccount.py
This module defines the CheckingAccount class.
"""

class CheckingAccount:
    """This class represents a checking account with name, PIN, and balance."""

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return None

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None

    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name

    def getPin(self):
        return self.pin
    
    def __str__(self):
        result =  'Type:    Checking\n'
        result += 'Name:    ' + self.name + '\n' 
        result += 'PIN:     ' + self.pin + '\n' 
        result += 'Balance: ' + str(self.balance)
        return result

def main():
    # 1. Test Instantiation
    print("--- Testing Instantiation ---")
    acct = CheckingAccount("June Zuo", "1234", 500.0)
    print("Account created successfully.\n")

    # 2. Test String Representation
    print("--- Testing String Representation ---")
    print(acct)
    print()
    
    # 3. Test Getters
    print("--- Testing Getters ---")
    print("Name:    ", acct.getName())
    print("PIN:     ", acct.getPin())
    print("Balance: ", acct.getBalance())
    print()

    # 4. Test Deposit
    print("--- Testing Deposit ---")
    acct.deposit(250.0)
    print("Deposited 250.0. New Balance: 750.0\n")

    # 5. Test Withdrawals 
    print("--- Testing Withdrawals ---")
    print("Withdrawing 100.0...")
    result = acct.withdraw(100.0)
    print("Result: None (None means success)")
    print("New Balance: 650.0\n")

    print("Withdrawing 1000.0 (Insufficient funds test)...")
    result = acct.withdraw(1000.0)
    print("Result:", result, "\n")

    print("Withdrawing -50.0 (Negative amount test)...")
    result = acct.withdraw(-50.0)
    print("Result:", result, "\n")

    # 6. Final State
    print("--- Final Account State ---")
    print(acct)

if __name__ == "__main__":
    main()