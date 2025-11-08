import tkinter

root = tkinter.Tk()

label1 = tkinter.Label(root, text="Left")
label1.pack(side="left")

label2 = tkinter.Label(root, text="Right")
label2.pack(side="right")

root.mainloop()