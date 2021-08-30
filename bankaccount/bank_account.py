class BankAccount:
    accounts = []

    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError(f"Cannot open account with {balance} balance")
        self.__balance = balance
        self.number = len(BankAccount.accounts)
        BankAccount.accounts.append(self)

    def prevent_negative_withdrawal(self, balance, amount):
        if balance - amount < 0:
            raise ValueError(
                f"Can't withdraw {amount} with {self.__balance} balance")

    @property
    def balance(self):
        return self.__balance

    def prevent_negative_deposit(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot deposit {amount}")

    def prevent_negative_transfer(self, amount):
        if amount < 0:
            raise ValueError(f"Cannot transfer {amount}")

    def deposit(self, amount):
        self.prevent_negative_deposit(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self.prevent_negative_withdrawal(self.__balance, amount)
        self.__balance -= amount

    def transfer(self, other_account, amount):
        self.prevent_negative_transfer(amount)
        self.prevent_negative_withdrawal(self.__balance, amount)
        self.withdraw(amount)
        other_account.deposit(amount)

    def __repr__(self):
        return f"BankAccount(balance={self.__balance})"
