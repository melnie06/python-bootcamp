import tkinter

root = tkinter.Tk()
items = tkinter.StringVar(value=["Item 1", "Item 2", "Item 3"])
listbox = tkinter.Listbox(
    root,
    listvariable=items,
    selectmode=tkinter.MULTIPLE,
)
listbox.pack()


def show_selection():
    selection = [listbox.get(index) for index in listbox.curselection()]
    print("Selected:", selection)


button = tkinter.Button(root, text="Show Selection", command=show_selection)
button.pack()
root.mainloop()
