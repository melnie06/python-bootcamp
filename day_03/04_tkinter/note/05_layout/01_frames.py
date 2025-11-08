import tkinter

root = tkinter.Tk()

left_frame = tkinter.Frame(root, bg="lightblue")
left_frame.pack(side="left")

left_label = tkinter.Label(left_frame, text="I'm on the left")
left_label.pack()

right_frame = tkinter.Frame(root, bg="lightgreen")
right_frame.pack(side="right")

right_entry = tkinter.Entry(right_frame)
right_entry.pack()

right_button = tkinter.Button(right_frame, text="Click me")
right_button.pack()

root.mainloop()


