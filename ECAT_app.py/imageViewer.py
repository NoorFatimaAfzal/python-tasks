from tkinter import *
from PIL import ImageTk, Image
root=Tk()

root.title("Image Viewer")
root.iconbitmap('ECAT_app.py/n.ico')
my_image1=ImageTk.PhotoImage(Image.open("ECAT_app.py/1.jpg"))
my_image2=ImageTk.PhotoImage(Image.open("ECAT_app.py/2.jpg"))
my_image3=ImageTk.PhotoImage(Image.open("ECAT_app.py/3.jpg"))
my_image4=ImageTk.PhotoImage(Image.open("ECAT_app.py/4.jpg"))
my_image5=ImageTk.PhotoImage(Image.open("ECAT_app.py/5.jpg"))
my_image6=ImageTk.PhotoImage(Image.open("ECAT_app.py/6.jpg"))

image_list=[my_image1, my_image2, my_image3, my_image4, my_image5, my_image6]

my_label=Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])

       

def back():
    global my_label
    global button_forward
    global button_back
    

button_back=Button(root, text="<<", command=back)
button_exit=Button(root, text="Exit", command=root.quit)
button_forward=Button(root, text=">>",command=lambda: button_forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)



root.mainloop()
