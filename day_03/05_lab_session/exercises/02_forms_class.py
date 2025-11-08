import tkinter as tk


class FormApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Feedback Form")

        # Form variables
        self.name_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.theme_var = tk.StringVar(value="Light")
        self.subscribe_var = tk.BooleanVar()
        self.rating_var = tk.IntVar(value=3)

        self.main_frame = tk.Frame(self)
        self.main_frame.grid()

        # Build sections
        self.build_name()
        self.build_age()
        self.build_theme()
        self.build_subscription()
        self.build_rating()
        self.build_submit_button()

    def build_name(self):
        """TODO"""

    def build_age(self):
        """TODO"""

    def build_theme(self):
        """TODO"""

    def build_subscription(self):
        """TODO"""

    def build_rating(self):
        """TODO"""

    def build_submit_button(self):
        """TODO"""

    def save_to_json(self):
        """TODO"""


if __name__ == "__main__":
    app = FormApp()
    app.mainloop()
