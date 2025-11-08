import tkinter

root = tkinter.Tk()
count = tkinter.IntVar(root, value=0)
label = tkinter.Label(root, textvariable=count)
label.pack()


def increment():
    new_value = count.get() + 1
    count.set(new_value)


# TODO: Add function to decrement count

increment_button = tkinter.Button(root, text=" + ", command=increment)
increment_button.pack(side="left")

# TODO: Add button to decrement

root.mainloop()
