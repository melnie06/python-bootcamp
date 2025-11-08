import tkinter
from tkinter import messagebox

root = tkinter.Tk()

# true or false
response = messagebox.askokcancel(
    "Ask OK/Cancel",
    "Do you want to proceed?"
)

root.mainloop()


