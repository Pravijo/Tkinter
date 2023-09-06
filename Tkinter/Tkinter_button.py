from tkinter import *
from tkinter import messagebox
obj = Tk()
obj.title("Button")
obj.geometry('300x300')


def m1():
    messagebox.showinfo("message", "Welcome to the page")


b1 = Button(obj, text="Click", command=m1)
b1.pack()

obj.mainloop()


