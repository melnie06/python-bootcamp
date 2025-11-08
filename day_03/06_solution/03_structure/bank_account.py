class BankAccount:

    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough money")

        self.__balance -= amount

    def deposit(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough money")

        self.__balance += amount


bank_account = BankAccount()
