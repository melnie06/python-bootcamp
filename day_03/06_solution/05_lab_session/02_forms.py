import json
import tkinter as tk
from tkinter import ttk  # Same as tk but cleaner


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

        self.main_frame = ttk.Frame(self, padding=20)
        self.main_frame.grid()

        # Build sections
        self.build_name()
        self.build_age()
        self.build_theme()
        self.build_subscription()
        self.build_rating()
        self.build_submit_button()

    def build_name(self):
        ttk.Label(self.main_frame, text="Name").grid(row=0, column=0, sticky="w", pady=5)
        ttk.Entry(self.main_frame, textvariable=self.name_var).grid(row=0, column=1, sticky="w")

    def build_age(self):
        ttk.Label(self.main_frame, text="Age").grid(row=1, column=0, sticky="w", pady=5)
        ttk.Entry(self.main_frame, textvariable=self.age_var).grid(row=1, column=1, sticky="w")

    def build_theme(self):
        ttk.Label(self.main_frame, text="Preferred Theme").grid(row=2, column=0, sticky="e", pady=5)
        theme_frame = ttk.Frame(self.main_frame)
        theme_frame.grid(row=2, column=1, sticky="w")
        ttk.Radiobutton(theme_frame, text="Light", variable=self.theme_var, value="Light").pack(side="left")
        ttk.Radiobutton(theme_frame, text="Dark", variable=self.theme_var, value="Dark").pack(side="left")

    def build_subscription(self):
        ttk.Checkbutton(self.main_frame, text="Subscribe to newsletter", variable=self.subscribe_var) \
            .grid(row=3, column=0, columnspan=2, pady=10)

    def build_rating(self):
        ttk.Label(self.main_frame, text="Rate us").grid(row=4, column=0, sticky="e", pady=5)
        ttk.Scale(self.main_frame, from_=1, to=5, variable=self.rating_var, orient="horizontal") \
            .grid(row=4, column=1, sticky="w")

    def build_submit_button(self):
        ttk.Button(self.main_frame, text="Submit", command=self.save_to_json) \
            .grid(row=5, column=0, columnspan=2, pady=10)

    def save_to_json(self):
        data = {
            "name": self.name_var.get(),
            "age": self.age_var.get(),
            "preferred_theme": self.theme_var.get(),
            "subscribe": self.subscribe_var.get(),
            "rating": self.rating_var.get()
        }

        with open("form_data.json", "w") as f:
            json.dump(data, f, indent=4)

        print("Form saved:", data)


if __name__ == "__main__":
    app = FormApp()
    app.mainloop()
