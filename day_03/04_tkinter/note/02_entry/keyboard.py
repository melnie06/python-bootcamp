
import tkinter

root = tkinter.Tk() #making the window

# entry = tkinter.Entry(root) #making the entry box
entry_var = tkinter.StringVar(root, value="")
entry = tkinter.Entry(root, textvariable=entry_var)
entry.pack()

label_var = tkinter.StringVar(root, value="")
label = tkinter.Label(root, textvariable=label_var)
label.pack()

def show_input(event=None):
    given_text = entry_var.get()
    label_var.set(given_text)
    


root.bind("<Return>", show_input) #root.bind (key, function_name)
# root.bind("<space>", show_input)
root.mainloop()