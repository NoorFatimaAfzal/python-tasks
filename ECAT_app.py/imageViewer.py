from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk

root = Tk()
root.title("Image Viewer")


# Get the screen height
screen_height = root.winfo_screenheight()

my_image1 = Image.open("ECAT_app.py/1.jpg")
my_image1_height = screen_height // 2
my_image1 = my_image1.resize((int(my_image1.width * (my_image1_height / my_image1.height)), my_image1_height),
                             Image.NEAREST)
my_image1 = ImageTk.PhotoImage(my_image1)

my_image2 = Image.open("ECAT_app.py/2.jpg")
my_image2 = my_image2.resize((int(my_image2.width * (my_image1_height / my_image2.height)), my_image1_height),
                             Image.NEAREST)
my_image2 = ImageTk.PhotoImage(my_image2)

my_image3 = Image.open("ECAT_app.py/3.jpg")
my_image3 = my_image3.resize((int(my_image3.width * (my_image1_height / my_image3.height)), my_image1_height),
                             Image.NEAREST)
my_image3 = ImageTk.PhotoImage(my_image3)

my_image4 = Image.open("ECAT_app.py/4.jpg")
my_image4 = my_image4.resize((int(my_image4.width * (my_image1_height / my_image4.height)), my_image1_height),
                             Image.NEAREST)
my_image4 = ImageTk.PhotoImage(my_image4)

my_image5 = Image.open("ECAT_app.py/5.jpg")
my_image5 = my_image5.resize((int(my_image5.width * (my_image1_height / my_image5.height)), my_image1_height),
                             Image.NEAREST)
my_image5 = ImageTk.PhotoImage(my_image5)

my_image6 = Image.open("ECAT_app.py/6.jpg")
my_image6 = my_image6.resize((int(my_image6.width * (my_image1_height / my_image6.height)), my_image1_height),
                             Image.NEAREST)
my_image6 = ImageTk.PhotoImage(my_image6)

image_list = [my_image1, my_image2, my_image3, my_image4, my_image5, my_image6]
status=Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_image1)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_forward.grid(row=1, column=2, pady=10, sticky=E)
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_back.grid(row=1, column=0, pady=10, sticky=W)
    status=Label(root, text="Image " + str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)



def back(image_number):
    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    my_label.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_forward.grid(row=1, column=2, pady=10, sticky=E)
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))
    button_back.grid(row=1, column=0, pady=10, sticky=W)
    status=Label(root, text="Image " + str(image_number) +" of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)


button_back = Button(root, text="<<", command=lambda: back(0))
button_exit = Button(root, text="Exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

button_back.grid(row=1, column=0, pady=10, sticky=W)
button_exit.grid(row=1, column=1, pady=10)
button_forward.grid(row=1, column=2, pady=10, sticky=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()