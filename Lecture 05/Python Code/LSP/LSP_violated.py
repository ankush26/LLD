# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 05\Python Code\LSP\LSP_violated.py
# This file illustrates a violation of the Liskov Substitution Principle (LSP).

class Account:
    def deposit(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")

    def withdraw(self, amount):
        raise NotImplementedError("Subclasses must implement this method.")

class SavingAccount(Account):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds in Savings Account!")

class CurrentAccount(Account):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError("Insufficient funds in Current Account!")

class FixedTermAccount(Account):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        raise NotImplementedError("Withdrawal not allowed in Fixed Term Account!")

def process_transactions(accounts):
    for acc in accounts:
        acc.deposit(1000)  # All accounts allow deposits
        try:
            acc.withdraw(500)  # Assuming all accounts support withdrawal (LSP Violation)
        except NotImplementedError as e:
            print(f"Exception: {e}")

# Example usage
if __name__ == "__main__":
    accounts = [SavingAccount(), CurrentAccount(), FixedTermAccount()]
    process_transactions(accounts)