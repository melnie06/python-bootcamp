import tkinter

root = tkinter.Tk()

slider_value = tkinter.IntVar(value=0)
slider = tkinter.Scale(
    root,
    from_=0,
    to=100,
    orient="horizontal",
    variable=slider_value
)
slider.pack()

root.mainloop()


