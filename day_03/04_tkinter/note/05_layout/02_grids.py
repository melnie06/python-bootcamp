import tkinter

root = tkinter.Tk()

top = tkinter.Label(root, text="Top", bg="blue", width=40, height=2)
top.grid(row=0, column=0, columnspan=3, sticky="nsew")

side = tkinter.Label(root, text="Side", bg="green", width=15, height=4)
side.grid(row=1, column=0, rowspan=2, sticky="nsew")

# Top Left
cell_1_1 = tkinter.Label(root, text="1,1", bg="gray", width=15, height=2)
cell_1_1.grid(row=1, column=1)

# Top Right
cell_1_2 = tkinter.Label(root, text="1,2", bg="gray", width=15, height=2)
cell_1_2.grid(row=1, column=2)

# Bottom Left
cell_2_1 = tkinter.Label(root, text="2,1", bg="yellow", width=15, height=2)
cell_2_1.grid(row=2, column=1)

# Bottom Right
cell_2_2 = tkinter.Label(root, text="2,2", bg="yellow", width=15, height=2)
cell_2_2.grid(row=2, column=2)

root.mainloop()


