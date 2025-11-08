import tkinter

root = tkinter.Tk()

label1 = tkinter.Label(
    root,
    text=":) Happy",
    font=("Arial", 25, "bold"),
    bg="green",
    fg="white",
    width=20,
    height=4,
)
label1.pack(side="left")

label2 = tkinter.Label(
    root,
    text=":( Sad",
    font=("Arial", 25, "italic"),
    bg="blue",
    fg="white",
    width=20,
    height=4,
)
label2.pack(side="right")

root.mainloop()
