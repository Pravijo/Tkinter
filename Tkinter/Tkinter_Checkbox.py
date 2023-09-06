from tkinter import *
obj = Tk()
obj.title("Check Box")
obj.geometry('300x300')

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()


cb1 = Checkbutton(obj, text="Car", variable=v1, onvalue=1, offvalue=0, height=3, width=6)
cb2 = Checkbutton(obj, text="Bike", variable=v2, onvalue=1, offvalue=0, height=3, width=6)
cb3 = Checkbutton(obj, text="Bicycle", variable=v3, onvalue=1, offvalue=0, height=3, width=6)

cb1.pack()
cb2.pack()
cb3.pack()


obj.mainloop()