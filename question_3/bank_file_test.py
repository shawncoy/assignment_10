"""
File: bank_file_test.py
Tests the pickle load/dump functionality for the updated Bank class.
"""
from bank_file import Bank
from savingsaccount import SavingsAccount
from checkingaccount import CheckingAccount
import os

# complete the main function to test the save/load functionality of the Bank class.
def main():
    test_file = "bank_data.dat"

    # --- Phase 1: Creating Bank and Adding Accounts ---
    print("--- Phase 1: Creating Bank and Adding Accounts ---")
    # Initialize an empty bank (no file loaded yet)
    bank1 = Bank()
    bank1.add(SavingsAccount("Alice", "1001", 1000.0))
    bank1.add(CheckingAccount("Bob", "2002", 500.0))
    
    print("Bank 1 (Original) State:")
    print(bank1)
    print()

    # --- Phase 2: Saving Bank to File ---
    print("--- Phase 2: Saving Bank to File ---")
    bank1.save(test_file)
    print(f"Bank saved to {test_file}")
    print()

    # --- Phase 3: Loading Data into a Fresh Bank Object ---
    print("--- Phase 3: Loading Data into a Fresh Bank Object ---")
    # This brand new object will look for the file in its __init__
    bank2 = Bank(test_file)
    print(f"Bank data loaded from {test_file}")
    
    print("Bank 2 (Loaded) State:")
    print(bank2)
    
if __name__ == "__main__":
    main()