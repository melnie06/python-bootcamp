import tkinter

class Application(tkinter.Tk):
    def __init__(self):
            super().__init__()
            self.title("Tkinter Class Structure")
            self.geometry("300x200")
            self.create_widgets()

    def create_widgets(self):
        label = tkinter.Button(self, text="Hello", command=self.hello)
        label.pack()

    def hello(self):
            print("Hello")

app = Application()
app.mainloop()


