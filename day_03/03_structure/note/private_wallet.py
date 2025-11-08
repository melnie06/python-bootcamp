class PrivateWallet:
    def __init__(self, initial_amount=0):
        self.__amount = initial_amount

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount > 10_000:
            raise ValueError("Amount Too Large")

        self.__amount = new_amount


budget = PrivateWallet()
budget.amount += 1000
print("Budget:", budget.amount)
