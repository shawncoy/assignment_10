"""
File: savingsaccount.py
Refactor savings account defined in question_1 based on the BankAccount parent class.
"""
from bankaccount import BankAccount
class SavingsAccount(BankAccount):
    RATE = 0.02  # Single rate for all accounts

    def __init__(self, name, pin, balance = 0.0):
        super().__init__(name, pin, balance)

    def computeInterest(self):
        """Computes, deposits, and returns the interest."""
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest

    def __str__(self):
        """Returns the string rep."""
        result =  'Type:    Savings\n'
        result += 'Name:    ' + self.name + '\n'
        result += 'PIN:     ' + self.pin + '\n'
        result += 'Balance: ' + str(self.balance)
        return result