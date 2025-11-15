class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount


class CreditPayment:
    def __init__(self, amount, limit):
        """Set attributes here"""
        self.amount = amount
        self.limit = limit

    def total(self):
        if self.amount > self.limit:
        # """Raise error if amount is beyond limit"""
            # return (f"Payment {self.limit} is beyond limit")
            raise ValueError ("Amount must be greater than or equal to limit") #shows the error
        return self.amount

class OnlinePayment:
    def __init__(self, amount, fee):
        self.amount = amount
        self.fee = fee
        """Set attributes here"""
        
    def __repr__(self):
        return f"Online payment (amount={self.amount}, fee={self.fee}, total={self.amount})"

    def total(self):
        """Return amount + fee"""
        # if self.amount + self.fee:
        return self.amount  + self.fee


class DiscountedPayment:
    def __init__(self, amount, discount):
        self.amount = amount
        self.discount = discount #(0.2)
        """Set attributes here"""

    def total(self):
        """Return amount - discount"""
        return self.amount - self.discount


payments = [
    CashPayment(1_000),
    CashPayment(10_000),
    CreditPayment(100_000, 145_000),
    OnlinePayment(5_000, 10_000),
    # DiscountedPayment()
]

for payment in payments:
    print(payment.total())
