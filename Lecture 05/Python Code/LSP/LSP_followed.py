# filepath: c:\Users\ankus\Desktop\LLD\LLD\Lecture 05\Python Code\LSP\LSP_followed.py
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
        print(f"Deposited: {amount} in Savings Account. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount} from Savings Account. New Balance: {self.balance}")
        else:
            print("Insufficient funds in Savings Account!")


class CurrentAccount(Account):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount} in Current Account. New Balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount} from Current Account. New Balance: {self.balance}")
        else:
            print("Insufficient funds in Current Account!")


class FixedTermAccount(Account):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount} in Fixed Term Account. New Balance: {self.balance}")

    def withdraw(self, amount):
        raise NotImplementedError("Withdrawal not allowed in Fixed Term Account!")


class BankClient:
    def __init__(self, accounts):
        self.accounts = accounts

    def process_transactions(self):
        for acc in self.accounts:
            acc.deposit(1000)  # All accounts allow deposits
            acc.withdraw(500)   # Assuming all accounts support withdrawal


# Example usage
if __name__ == "__main__":
    accounts = [SavingAccount(), CurrentAccount(), FixedTermAccount()]
    client = BankClient(accounts)
    client.process_transactions()