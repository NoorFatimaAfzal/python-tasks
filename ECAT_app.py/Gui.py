from tkinter import *
root=Tk()
mylabel=Label(root, text="Welcome to ECAT Test", font=("Arial", 20))

def myclick():
    mylabel=Label(root, text="Button clicked")
    mylabel.pack()
mybutton=Button(root, text="Click me", fg="white", bg="black", padx=50, pady=20, command=myclick ,foreground="white", background="black", font="Arial 20 bold", borderwidth=5)
mybutton.pack()

e=Entry(root, width=50, bg="black", fg="white", borderwidth=5)
e.pack()
e.insert(0, "Enter your name")

root.minsize(400,400)
mylabel.pack()
root.mainloop()
