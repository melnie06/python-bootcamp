import tkinter


root = tkinter.Tk()


# TODO: Add label for instructions
label_var = tkinter.StringVar(root, value="Enter your password")
label = tkinter.Label(root, textvariable=label_var)
label.pack()

# TODO: Add entry for instructions
entry_var = tkinter.StringVar(root, value="")
entry = tkinter.Entry(root, textvariable=entry_var)
entry.pack()


label_var = tkinter.StringVar(root, value="Enter your password and press Enter") # TODO: Add StringVar for instruction
label = tkinter.Label(root, textvariable=label_var) # TODO: Add label using StringVar
label.pack()




def check_password(event=None):
    password = "Test123"
    if entry_var.get() == password:
        label_var.set("Password correct Access granted")
    else:
        label_var.set("Incorrect password. Try again")
    
        
button = tkinter.Button(root, text="Submit", command=check_password)
button.pack()


# TODO: Check if entry.get() has correct value

# TODO: Add key bindings for check_password


root.bind("<Return>", check_password) 
root.mainloop()
