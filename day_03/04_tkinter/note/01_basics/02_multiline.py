import tkinter

root = tkinter.Tk()

message = """
Hello
World
"""

label = tkinter.Label(root, text=message)
label.pack()

root.mainloop()