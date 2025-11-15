class ProtectedWallet:
    def __init__(self, initial_amount=0):
        self._amount = initial_amount

    @property
    def amount(self):
        return self._amount
    
    
    def set_amount(self, new_amount):
        self._amount = new_amount

budget = ProtectedWallet()
budget._amount += 1000
print("Budget:", budget.amount)