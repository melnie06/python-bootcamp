class Wallet:
    def __init__(self, initial_amount=0):
        self.amount = initial_amount


transport_wallet = Wallet(500)
print("Transport Budget:", transport_wallet.amount)

food_wallet = Wallet()
food_wallet.amount += 300
print("Food Budget:", food_wallet.amount)
