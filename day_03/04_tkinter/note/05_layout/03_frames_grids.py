import tkinter

root = tkinter.Tk()
root.title("Login Form")

form_frame = tkinter.Frame(root, padx=20, pady=20)
form_frame.pack()

tkinter.Label(form_frame, text="Username:").grid(row=0, column=0)
username_entry = tkinter.Entry(form_frame)
username_entry.grid(row=0, column=1)

tkinter.Label(form_frame, text="Password:").grid(row=1, column=0)
password_entry = tkinter.Entry(form_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tkinter.Button(form_frame, text="Login")
login_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()



