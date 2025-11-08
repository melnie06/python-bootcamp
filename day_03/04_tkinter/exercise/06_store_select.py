import tkinter

root = tkinter.Tk()

instructions = tkinter.Label(root, text="Choose your favorite fruit:")
instructions.pack()

# TODO: Add radio buttons
radio_var = None

output_str = tkinter.StringVar(value="You chose: None")
output = tkinter.Label(root, textvariable=output_str)
output.pack()


def pick():
    chosen = radio_var.get()
    output_str.set("You chose: " + chosen)


button = tkinter.Button(root, text="Submit", command=pick)
button.pack()

root.mainloop()
