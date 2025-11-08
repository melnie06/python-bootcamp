import tkinter as tk


class CalculatorApp:
    """
    A simple calculator GUI using Tkinter.

    Features:
    - Supports basic arithmetic: +, -, *, /
    - Has "Clear" and "=" functions
    - Uses `eval()` to evaluate expressions (safe for this simple case)
    """

    def __init__(self):
        # Create the main window
        self.window = tk.Tk()
        self.window.title("Simple Calculator")

        # Holds the current expression as a string
        self.expression: str = ""

        # Create the display label
        self.display = tk.Label(
            self.window,
            text="",
            anchor="e",
            bg="white",
            fg="black",
            height=2,
            width=25,
            font=("Arial", 18)
        )
        self.display.grid(row=0, column=0, columnspan=4)

        # Set up all calculator buttons
        self.setup_buttons()

    def press(self, value: str) -> None:
        """Appends a digit or operator to the expression and updates display."""
        self.expression += value
        self.update_display()

    def clear(self) -> None:
        """Clears the expression."""
        self.expression = ""
        self.update_display()

    def calculate(self) -> None:
        """Evaluates the expression and updates the display."""
        try:
            result = eval(self.expression)
            self.expression = str(result)
        except Exception:
            self.expression = "Error"
        self.update_display()

    def update_display(self) -> None:
        """Updates the label to show the current expression."""
        self.display.config(text=self.expression)

    def make_button(self, text: str, row: int, column: int) -> None:
        """Creates and places a button in the grid."""
        if text == "C":
            command = self.clear
        elif text == "=":
            command = self.calculate
        else:
            command = lambda t=text: self.press(t)

        button = tk.Button(
            self.window,
            text=text,
            width=5,
            height=2,
            font=("Arial", 16),
            command=command
        )
        button.grid(row=row, column=column, padx=5, pady=5)

    def setup_buttons(self) -> None:
        """Creates and places all calculator buttons."""
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for text, row, col in buttons:
            self.make_button(text, row, col)

    def run(self) -> None:
        """Starts the main event loop."""
        self.window.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
