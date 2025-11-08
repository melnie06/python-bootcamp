import tkinter

root = tkinter.Tk()

label_value = tkinter.StringVar(value="")
check_value = tkinter.BooleanVar()


def greeting():
    if check_value.get():
        label_value.set("Hello")
    else:
        label_value.set("")


# TODO: Add checkbox button buttons

label = tkinter.Label(root, textvariable=label_value)
label.pack()

root.mainloop()
