

import tkinter

root = tkinter.Tk()

entry = tkinter.Entry(root)
entry.pack()




# def show_input(event):
# 	given_text = entry.get()
# 	label = tkinter.Label(root, text=given_text)
# 	label.pack()

root.bind("<Return>", show_input) #root.bind (key, function_name)
# root.bind("<space>", show_input)
root.mainloop()

