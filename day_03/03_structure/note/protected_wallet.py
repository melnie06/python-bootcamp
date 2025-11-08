class ProtectedWallet:
    def __init__(self, initial_amount=0):
        self._amount = initial_amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        if new_amount > 10_000:
            raise ValueError("Amount Too Large")

        self._amount = new_amount


budget = ProtectedWallet()
budget.amount += 1000
print("Budget:", budget.amount)
