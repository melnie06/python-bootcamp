def spend(expenses):
    """Add a new cost in expenses"""
    new_expense = float(input("Enter new expense: "))
    expenses.append(new_expense)
    print(f"Added PHP {new_expense} to expenses")


def refund(expenses):
    """Remove the last cost added (if any)"""
    if expenses:
        refunded = expenses.pop(-1)
        print(f"Refunded PHP {refunded}")
    else:
        print("No expenses yet")


def show(expenses):
    """Print the current list of expenses and total"""
    print(f"Expenses: (total PHP{sum(expenses)})")
    for number, expense in enumerate(expenses, start=1):
        print(f"\tExpense {number}:\tPHP {expense}")


def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        elif command == "refund":
            refund(current_expenses)
        elif command == "show":
            show(current_expenses)
        elif command == "exit":
            running = False


main()
