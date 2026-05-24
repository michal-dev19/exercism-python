"""Module to create a bank account with various functions"""


class BankAccount:
    """Class representing a bank account"""

    def __init__(self):
        self.balance = 0
        self.opened = False

    def get_balance(self):
        """Display balance of a bank account"""

        if not self.opened:
            raise ValueError("account not open")
        if self.opened:
            return self.balance
        return

    def open(self):
        """Open bank account if it is not yet opened"""

        if not self.opened:
            self.opened = True
            return
        raise ValueError("account already open")

    def deposit(self, amount):
        """Deposit an amount into a bank account"""

        if amount < 0:
            raise ValueError("amount must be greater than 0")
        if not self.opened:
            raise ValueError("account not open")
        self.balance += amount

    def withdraw(self, amount):
        """Withdraw an amount out of a bank account"""

        if not self.opened:
            raise ValueError("account not open")
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        if self.balance < amount:
            raise ValueError("amount must be less than balance")
        self.balance -= amount

    def close(self):
        """Close bank account if it is not yet closed"""

        if not self.opened:
            raise ValueError("account not open")
        self.opened = False
        self.balance = 0
