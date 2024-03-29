import tkinter as tk

window = tk.Tk()

window.geometry('500x500')
window.title('My First GUI')

# The Label() function is used to create a text
label = tk.Label(window, text='Hello World!', font=('Arial', 18))
label.pack(padx=20, pady=20)

# The function Text() is used to create a plaform in which you can type multiple lines.
textbox = tk.Text(window, height=3, font=('Arial', 16))
textbox.pack(padx=10, pady=10)

# The Button() function is used to create a button.
# button = tk.Button(window, text='Click Me!', font=('Arial', 16))
# button.pack(padx=10, pady=10)

# The function Entry() is used to create a platform that doesn't allow multi-line e.g for passwords
# my_entry = tk.Entry(window)
# my_entry.pack(padx=10)

buttonframe = tk.Frame(window)
buttonframe.columnconfigure(0, weight=1 )
buttonframe.columnconfigure(1, weight=1 )
buttonframe.columnconfigure(2, weight=1 )

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 18))
btn1.grid(row=0, column=0, sticky= tk.W+tk.E)# row=0 and colum=0 refers to the first row and column while the sticky param is to allow the btns strech equally from west to east.

btn2 = tk.Button(buttonframe, text='2', font=('Arial', 18))
btn2.grid(row=0, column=1, sticky= tk.W+tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Arial', 18))
btn3.grid(row=0, column=2, sticky= tk.W+tk.E)

btn4 = tk.Button(buttonframe, text='4', font=('Arial', 18))
btn4.grid(row=1, column=0, sticky= tk.W+tk.E)

btn5 = tk.Button(buttonframe, text='5', font=('Arial', 18))
btn5.grid(row=1, column=1, sticky= tk.W+tk.E)

btn6 = tk.Button(buttonframe, text='6', font=('Arial', 18))
btn6.grid(row=1, column=2, sticky= tk.W+tk.E)
 
# anotherbtn = tk.Button(window, text='TEST', font=('Arial', 17))
# anotherbtn.place(x=0, y=0, height=500, width=500)
buttonframe.pack(fill='x')# fill='x' means the buttonframe is going to strech in the x direction
window.mainloop()
