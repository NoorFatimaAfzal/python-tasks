from tkinter import *
from PIL import ImageTk, Image
root=Tk()

root.title("learning tkinter")
root.iconbitmap('ECAT_app.py/n.ico')


my_img1=ImageTk.PhotoImage(Image.open("ECAT_app.py/n.ico"))
my_label=Label(image=my_img1) 
my_label.pack()

quit_button=Button(root, text="Exit", command=root.quit)
quit_button.pack()

root.mainloop()
