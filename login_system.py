from tkinter import *
from PIL import ImageTk
class Login():
    def __init__(self, root):
        self.root = root
        # To set the title of the interface
        self.root.title("Login System")
        # Setting the size of the interface
        self.root.geometry("1199x688+200+100")
        

        # To set up backgroung image
        self.bg = ImageTk.PhotoImage(file='pics/image.jpg')
        self.bg_image = Label(self.root, image=self.bg).place(x=100,y=100, relwidth=1199, relheight=688)

root = Tk()
object = Login(root)
root.mainloop()