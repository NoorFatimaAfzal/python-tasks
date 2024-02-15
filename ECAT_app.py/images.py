from tkinter import *
root=Tk()
#i want to make a quiz app
question=Label(root, text="What is the capital of France?", font=("Arial", 20))
question.pack()
def check(number):
    if number==1:
        print("Correct")
    else:
        print("Incorrect")
        


#make buttons
button1=Checkbutton(root, text="Paris", padx=40, pady=20,command=lambda: check(1))
button2=Checkbutton(root, text="London", padx=40, pady=20,command=lambda: check(2))
button3=Checkbutton(root, text="Berlin", padx=40, pady=20,command=lambda: check(3))
button4=Checkbutton(root, text="Madrid", padx=40, pady=20,command=lambda: check(4))
button1.pack()
button2.pack()
button3.pack()
button4.pack()
#make a skip button
skip_button=Button(root, text="Skip", padx=40, pady=20, )
skip_button.pack()
#make a submit button
submit_button=Button(root, text="Submit", padx=40, pady=20)
submit_button.pack()





root.mainloop()
