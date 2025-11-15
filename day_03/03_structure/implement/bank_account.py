class NegativeDepositError(ValueError):
    def __init__(self, amount):
        message = f"Negative amount {amount} is not allowed"
        super().__init__(message)


# class NegativeDeposit(Exception):
#     pass
class NegativeWithdraw(Exception):
    pass
    
class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance


    def deposit(self, amount):
        # if amount > 0:
        #     print({BankAccount})
        if amount < 0:
            raise NegativeDepositError(amount)
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise NegativeWithdraw("Must not be negative withdraw")

        if amount > self._balance:
            raise NegativeWithdraw("Must not be negative withdraw")

    def print_balance(self):
        print(self._balance)


bank_account = BankAccount(1000)
bank_account.deposit(-100)
# print(bank_account)
# bank_account.withdraw(1_000_000)
