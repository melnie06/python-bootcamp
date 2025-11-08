class CashPayment:
    def __init__(self, amount):
        self.amount = amount

    def total(self):
        return self.amount


class CreditPayment:
    def __init__(self, amount, limit):
        self.amount = amount
        self.limit = limit

    def total(self):
        if self.amount > self.limit:
            raise ValueError("Amount too high")

        return self.amount


class OnlinePayment:
    def __init__(self, amount, fee):
        self.amount = amount
        self.fee = fee

    def total(self):
        return self.amount + self.fee


class DiscountedPayment:
    def __init__(self, amount, discount):
        self.amount = amount
        self.discount = discount

    def total(self):
        return self.amount - self.discount


payments = [
    CashPayment(1_000),
    CreditPayment(1_000, 1_000),
    OnlinePayment(1_000, 1_000),
    DiscountedPayment(1_000, 1_000),
]

for payment in payments:
    print(payment.total())
