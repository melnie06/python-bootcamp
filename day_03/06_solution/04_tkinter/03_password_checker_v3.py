import tkinter
from tkinter import messagebox

root = tkinter.Tk()

instruction = tkinter.Label(root, text="Enter your password:")
instruction.pack()

entry = tkinter.Entry(root)
entry.pack()

output = tkinter.StringVar(root, value="Enter your password and Submit")
output_label = tkinter.Label(root, textvariable=output)
output_label.pack()


def check_password():
    correct_password = "pass"

    if entry.get().lower() == correct_password:
        output_label["fg"] = "green"
        output.set("Password Correct! Access granted.")
    else:
        output_label["fg"] = "red"
        output.set("Incorrect password. Try again.")

        messagebox.showerror(
            "Error",
            "Incorrect password"
        )


button = tkinter.Button(root, text="Submit", command=check_password)
button.pack()

root.mainloop()
