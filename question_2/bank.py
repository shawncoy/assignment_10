"""
File: bank.py
A simplified version of the Bank class focusing on polymorphism 
and the BankAccount hierarchy.
"""
from savingsaccount import SavingsAccount 

class Bank:
    def __init__(self):
        """Initializes an empty bank."""
        self.accounts = {}

    def makeKey(self, name, pin, accountType):
        """Creates a unique key by appending the account type."""
        return name + pin + accountType

    def add(self, account):
        """Adds an account to the bank using a type-aware key."""
        acc_type = type(account).__name__
        key = self.makeKey(account.getName(), account.getPin(), acc_type)
        self.accounts[key] = account

    def get(self, name, pin, accountType):
        """Retrieves a specific account type."""
        key = self.makeKey(name, pin, accountType)
        return self.accounts.get(key, None)

    def remove(self, name, pin, accountType):
        """Removes and returns a specific account type."""
        key = self.makeKey(name, pin, accountType)
        return self.accounts.pop(key, None)

    def computeInterest(self):
        """
        Polymorphically computes interest.
        Only calls computeInterest on objects that are SavingsAccounts.
        """
        total = 0.0
        for account in self.accounts.values():
            if isinstance(account, SavingsAccount): 
                total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys currently in the bank."""
        return sorted(self.accounts.keys())

    def __str__(self):
        """Returns a string representation of all accounts."""
        if not self.accounts:
            return "The bank is empty."
        sorted_keys = self.getKeys()
        return "\n----------------\n".join([str(self.accounts[k]) for k in sorted_keys])