class BankAccount:
    def __init__(self, balance):
        if balance < 0:
            raise ValueError("Balance can't be negative")
        self.balance = balance

    def withdraw(self, amount):
        if self.balance - amount < 0:
            raise RuntimeError("Insufficient funds")
        self.balance -= amount
        print(f"Amount withdrawn. Remaining balance is {self.balance}")

class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        raise RuntimeError("Withdraw not allowed in Fixed Deposit")

# Example usage
if __name__ == "__main__":
    account = BankAccount(100)
    account.withdraw(100)

    fixed_account = FixedDepositAccount(200)
    try:
        fixed_account.withdraw(50)
    except RuntimeError as e:
        print(e)