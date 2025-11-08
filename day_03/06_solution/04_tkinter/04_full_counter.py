import tkinter

root = tkinter.Tk()
count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()


def increment():
    new_value = count.get() + 1
    count.set(new_value)


def decrement():
    new_value = count.get() - 1
    if new_value >= 0:
        count.set(new_value)


increment_button = tkinter.Button(root, text=" + ", command=increment)
increment_button.pack(side="left")

decrement_button = tkinter.Button(root, text=" - ", command=decrement)
decrement_button.pack(side="right")

root.mainloop()
