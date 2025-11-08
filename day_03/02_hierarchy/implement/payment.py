class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount


class CreditPayment:
    def __init__(self, amount, limit):
        """Set attributes here"""

    def total(self):
        """Raise error if amount is beyond limit"""


class OnlinePayment:
    def __init__(self, amount, fee):
        """Set attributes here"""

    def total(self):
        """Return amount + fee"""


class DiscountedPayment:
    def __init__(self, amount, discount):
        """Set attributes here"""

    def total(self):
        """Return amount - discount"""


payments = [
    CashPayment(1_000)
]

for payment in payments:
    print(payment.total())
