"""
File: bank_v2.py
Reengineered to support BankAccount hierarchy and polymorphic behavior.
"""
import pickle

class Bank:
    def __init__(self, fileName = None):
        """Initializes the bank and loads data if a file is provided."""
        self.accounts = {}
        self.fileName = fileName
        if fileName is not None:
            try:
                with open(fileName, 'rb') as f:
                    self.accounts = pickle.load(f)
            except (FileNotFoundError, EOFError):
                self.accounts = {}

    def makeKey(self, name, pin, accountType):
        """Makes and returns a key from name, pin, and account type."""
        return f"{name}/{pin}/{accountType}"

    def add(self, account):
        """Inserts an account using its specific type in the key."""
        accountType = type(account).__name__
        key = self.makeKey(account.getName(), account.getPin(), accountType)
        self.accounts[key] = account

    def remove(self, name, pin, accountType):
        """Removes and returns the specific account type, or None."""
        key = self.makeKey(name, pin, accountType)
        return self.accounts.pop(key, None)

    def get(self, name, pin, accountType):
        """Returns the specific account type, or None."""
        key = self.makeKey(name, pin, accountType)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Polymorphically computes interest only for applicable accounts."""
        total = 0.0
        for account in self.accounts.values():
            if hasattr(account, 'computeInterest'):
                total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of all account keys."""
        return sorted(self.accounts.keys())

    def save(self, fileName = None):
        """Saves the bank accounts to a file using pickle."""
        if fileName is not None:
            with open(fileName, 'wb') as f:
                pickle.dump(self.accounts, f)

    def __str__(self):
        """Returns the string representation of all accounts sorted by key."""
        if not self.accounts:
            return "The bank is empty."
        sorted_keys = self.getKeys()
        return "\n----------------\n".join([str(self.accounts[k]) for k in sorted_keys])