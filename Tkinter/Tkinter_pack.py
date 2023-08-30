import tkinter
from tkinter import *
obj = tkinter.Tk()
obj.geometry('400x400')
obj.title("Registration Form")

tb = Button(obj, text="start", height=1, width=6, fg="green", bg="grey")
tb.pack(side="top")

bb = Button(obj, text="Finish", height=1, width=6, fg="green", bg="grey")
bb.pack(side="bottom")

heading_label = tkinter.Label(obj, text="Registration form", font=("ariel",30,"bold"))
heading_label.pack(side="top")

obj.mainloop()

