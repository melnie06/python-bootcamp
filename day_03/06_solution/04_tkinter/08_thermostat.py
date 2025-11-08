import tkinter

root = tkinter.Tk()

warning = tkinter.StringVar(value="")
temperature = tkinter.IntVar(value=25)


def boiling_warning(event):
    boiling_point = 100
    if temperature.get() >= boiling_point:
        warning.set("Boiling point!")
    else:
        warning.set("")


tkinter.Label(root, text="Thermostat (Celsius)").pack()

slider = tkinter.Scale(
    root,
    from_=-200,
    to=+200,
    orient="horizontal",
    variable=temperature,
    command=boiling_warning
)
slider.pack()

tkinter.Label(root, textvariable=warning).pack()

root.mainloop()
