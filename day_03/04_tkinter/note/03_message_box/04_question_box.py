import tkinter
from tkinter import messagebox

root = tkinter.Tk()

# yes or no
response = messagebox.askquestion(
    "Question",
    "Do you want to continue?"
)

root.mainloop()


