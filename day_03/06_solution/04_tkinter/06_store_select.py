import tkinter

root = tkinter.Tk()

instructions = tkinter.Label(root, text="Choose your favorite fruit:")
instructions.pack()

radio_var = tkinter.StringVar(value="Option A")
radio1 = tkinter.Radiobutton(root, text="Apple", variable=radio_var, value="Apple")
radio1.pack()

radio2 = tkinter.Radiobutton(root, text="Banana", variable=radio_var, value="Banana")
radio2.pack()

radio3 = tkinter.Radiobutton(root, text="Mango", variable=radio_var, value="Mango")
radio3.pack()

output_str = tkinter.StringVar(value="You chose: None")
output = tkinter.Label(root, textvariable=output_str)
output.pack()


def pick():
    chosen = radio_var.get()
    output_str.set("You chose: " + chosen)


button = tkinter.Button(root, text="Submit", command=pick)
button.pack()

root.mainloop()
