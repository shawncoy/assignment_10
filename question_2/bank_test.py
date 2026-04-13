from bank import Bank
from checkingaccount import CheckingAccount
from savingsaccount import SavingsAccount

def main():
    bank = Bank()

    bank.add(CheckingAccount("June", "1111", 500.0))
    bank.add(SavingsAccount("June", "1111", 1000.0))
    
    print("--- Adding Accounts ---")
    # Added 'f' before the quotes to make it an f-string
    print(f"Keys in bank: {bank.getKeys()}")
    print()

    # 2. Test Polymorphic Interest
    print("--- Computing Interest ---")
    interest_paid = bank.computeInterest()
    print(f"Total interest paid: {interest_paid}")
    print()

    # 3. Test Retrieval
    print("--- Testing Retrieval ---")
    checking = bank.get("June", "1111", "CheckingAccount")
    if checking:
        print(f"Retrieved Balance: {checking.getBalance()}")
    print()

    # 4. Show final state
    print("--- Final Bank State ---")
    print(bank)

if __name__ == "__main__":
    main()