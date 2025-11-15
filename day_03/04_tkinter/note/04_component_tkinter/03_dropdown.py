import tkinter

root = tkinter.Tk()

options = ["Choice 1", "Choice 2", "Choice 3"]
dropdown_var = tkinter.StringVar(value="Choice 1")
dropdown_menu = tkinter.OptionMenu(root, dropdown_var, *options)
dropdown_menu.pack()

root.mainloop()
