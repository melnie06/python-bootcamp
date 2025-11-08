import tkinter

root = tkinter.Tk()

check_value = tkinter.BooleanVar()
checkbox = tkinter.Checkbutton(
    root,
    text="Enable",
    variable=check_value
)
checkbox.pack()

root.mainloop()
