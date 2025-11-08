import tkinter

mood_message_map = {
    "Sleepy": "Get that rest",
    "Productive": "Keep it up",
    "Hungry": "Eat up fam",
    "Stressed": "Chill dawg",
}

root = tkinter.Tk()

instructions = tkinter.Label(root, text="What's your current mood?")
instructions.pack()

# TODO: Add dropdown
dropdown_var = None

vibe_str = tkinter.StringVar(value="Your vibe will appear here...")
vibe = tkinter.Label(root, textvariable=vibe_str)
vibe.pack()


def pick():
    vibe_str.set(mood_message_map[dropdown_var.get()])


button = tkinter.Button(root, text="Check Vibe", command=pick)
button.pack()

root.mainloop()
