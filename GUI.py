from tkinter import *

root = Tk()

def myclick():
    myLabel = Label(root, text="you clicked this button")
    myLabel.pack()

myButton = Button(root, text="click me", padx = 50, pady=50, command=myclick, bg="blue", fg="red")
myButton.pack()
root.mainloop()