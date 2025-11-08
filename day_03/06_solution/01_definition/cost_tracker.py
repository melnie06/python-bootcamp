class CostTracker:
    def __init__(self):
        """Initialize with an empty expenses list"""
        self.expenses = []

    def spend(self):
        """Add a new cost in expenses"""
        new_expense = float(input("Enter new expense: "))
        self.expenses.append(new_expense)
        print(f"Added PHP {new_expense} to expenses")

    def refund(self):
        """Remove the last cost added (if any)"""
        if self.expenses:
            refunded = self.expenses.pop(-1)
            print(f"Refunded PHP {refunded}")
        else:
            print("No expenses yet")

    def show(self):
        """Print the current list of expenses and total"""
        print(f"Expenses: (total PHP{sum(self.expenses)})")
        for number, expense in enumerate(self.expenses, start=1):
            print(f"\tExpense {number}:\tPHP {expense}")

    def save(self, filename="expenses.txt"):
        """Save the current list of expenses in a file"""
        with open(filename, "w") as file:
            for expense in self.expenses:
                file.write(f"{expense}\n")
        print(f"Saved expenses to {filename}")

    def load(self, filename="expenses.txt"):
        """Load expenses from a file"""
        self.expenses = []
        try:
            with open(filename, "r") as file:
                for line in file.read().splitlines():
                    self.expenses.append(float(line))
            print(f"Loaded expenses from {filename}")
        except FileNotFoundError:
            print("No saved expenses found.")

    def mainloop(self):
        """Run the command loop"""
        running = True
        while running:
            command = input("Command: ").strip().lower()
            if command == "spend":
                self.spend()
            elif command == "refund":
                self.refund()
            elif command == "show":
                self.show()
            elif command == "save":
                self.save()
            elif command == "load":
                self.load()
            elif command == "exit":
                running = False
            else:
                print("Unknown command")


if __name__ == "__main__":
    tracker = CostTracker()
    tracker.mainloop()
