from dataclasses import dataclass
@dataclass
class BankAccount:
    account_number: str
    owner: str
    balance: float = 0.0

    def deposit(self, amount: float):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₱{amount}. New balance: ₱{self.balance}")

    def withdraw(self, amount: float):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ₱{self.balance}")

    def display_balance(self):
        print(f"Account Balance for {self.owner}: ₱{self.balance}")

account = BankAccount("123456", "Ramil", 10000)
account.deposit(1000)
account.withdraw(1000)
account.display_balance()