import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()

user_input = tkinter.StringVar(root, value="Enter any text")
label = tkinter.Label(root, textvariable=user_input)
label.pack()

def show_input():
    given_text = entry.get()
    user_input.set(given_text)

button = tkinter.Button(root, text="Submit", command=show_input)
button.pack()
root.mainloop()