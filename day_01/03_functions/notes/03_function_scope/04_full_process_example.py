def get_balance():
    return float(input("Enter your balance: "))


def get_withdrawal():
    return float(input("Enter amount to withdraw: "))


def process_withdrawal(balance, amount):
    if amount > balance:
        return "Insufficient funds!"
    return f"Success. Remaining: {balance - amount}"


current_balance = get_balance()
current_amount = get_withdrawal()
print(process_withdrawal(current_balance, current_amount))
