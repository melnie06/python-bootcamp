import tkinter

root = tkinter.Tk()

label_value = tkinter.StringVar(value="")
check_value = tkinter.BooleanVar()


def greeting():
    if check_value.get():
        label_value.set("Hello")
    else:
        label_value.set("")


checkbox = tkinter.Checkbutton(
    root,
    text="Enable",
    variable=check_value,
    command=greeting
)
checkbox.pack()

label = tkinter.Label(root, textvariable=label_value)
label.pack()

root.mainloop()
