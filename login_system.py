from tkinter import *
from PIL import ImageTk, Image
class Login():
    def __init__(self, root):
        self.root = root
        # To set the title of the interface
        self.root.title("Login System")
        # Setting the size of the interface
        self.root.geometry("1199x688+200+100")
        # Prevent window from maximazing.
        self.root.resizable(False, False)
        
        # To set up backgroung image
        self.background = ImageTk.PhotoImage(file='image_2.jpg') # To open the pic we want to use as the window background
        self.background_image = Label(self.root, image=self.background)
        self.background_image.place(x=0,y=0, relwidth=1, relheight=1)
        
        # Login Frame
        Frame_login = Frame(self.root, bg='white')
        Frame_login.place(x=330, y=150, width=500, height=400)

        # Content of the login frame.
        title =  Label(Frame_login, text="Login Here", font=('Impact', 35, 'bold'), fg="#6162FF", bg='white').place(x=90, y=30)
        sub_title =  Label(Frame_login, text="Members Login Area", font=('Goudy old style', 15, 'bold'), fg="#1d1d1d", bg='white').place(x=90, y=100)
       
        #  Username
        lbl_user =  Label(Frame_login, text="Username", font=('Goudy old style', 15, 'bold'), fg="grey", bg='white').place(x=90, y=140)
        self.username =  Entry(Frame_login,font=('Goudy old style', 15), bg='#E7E6E6')
        self.username.place(x=90, y=170, width=320, height=35)


root = Tk()
obj = Login(root)
root.mainloop()
