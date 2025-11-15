import tkinter

root = tkinter.Tk()

text = tkinter.StringVar(root, value="Hello")
label =tkinter.Label(root,textvariable=text)
label.pack()

root.mainloop()