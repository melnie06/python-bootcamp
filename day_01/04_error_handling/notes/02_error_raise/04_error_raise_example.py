def withdraw(balance, amount):
    if balance < amount:
        raise ValueError("Insufficient funds")
    if amount < 0:
        raise ValueError("Withdraw amount must be positive")

    new_balance = balance - amount
    return new_balance
