class CostTracker:
    def __init__(self):
        self.running = True
        self.current_expenses = []
        

    def spend(self):
        new_expense = float(input("Enter new expense: "))
        self.current_expenses.append(new_expense)
        print(f"Added PHP {new_expense} to expenses")

    def refund(self):
        if self.current_expenses:
            refunded = self.current_expenses.pop(-1)
            print(f"Refunded PHP {refunded}")
        else:
            print("No expenses yet")


    def shows(self):
        # print(f"Expenses: (total PHP {sum(self.current_expenses)})")
        print(f"Expenses: Total PHP {sum(self.current_expenses)}")
        for number, expense in enumerate(self.current_expenses, start=1):
            print(f"\tExpense {number}:\tPHP {expense}")

    
    
    def main_loop(self):
        
        while self.running:
            command = input("Command: ")
            if command == "spend":
                self.spend()
            elif command == "refund":
                self.refund()
            elif command == "show":
                self.shows()
            elif command == "exit":
                self.running = False
        
cost_tracker = CostTracker()
cost_tracker.main_loop()