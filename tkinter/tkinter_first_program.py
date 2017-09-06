from tkinter import *
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    # creation of init_window
    def init_window(self):
        self.master.title("This is a nice window!")
        self.pack(fill=BOTH, expand=1)
        # quitButton = Button(self, text="Quit", command=self.client_exit)
        # quitButton.place(x=20, y=20)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Option1", command=self.client_exit)
        file.add_command(label="Option2", command=self.client_exit)
        file.add_command(label="Option3", command=self.client_exit)
        file.add_command(label="Option4", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)
        edit.add_command(label="Undo", command=self.client_undo)
        edit.add_command(label="Show Image", command=self.show_image)
        edit.add_command(label="Show Text", command=self.show_text)
        menu.add_cascade(label="Edit", menu=edit)

    def client_undo(self):
        print("Undo button pressed")

    def client_exit(self):
        exit()

    def show_image(self):
        load = Image.open("image.png")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

    def show_text(self):
        text = Label(self, text="Hey there!")
        text.pack()



root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()
