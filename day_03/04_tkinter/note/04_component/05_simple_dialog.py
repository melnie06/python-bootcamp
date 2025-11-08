import tkinter
from tkinter import simpledialog

root = tkinter.Tk()

def ask_all():
    name = simpledialog.askstring("String", "Your name?")
    age = simpledialog.askinteger("Integer", "Your age?")
    score = simpledialog.askfloat("Float", "Your score?")
    if name and age and score:
        message = f"{name} | {age} | {score}"
        tkinter.Label(root, text=message).pack()

tkinter.Button(root, text="Start", command=ask_all).pack()
root.mainloop()


