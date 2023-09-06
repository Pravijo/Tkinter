from tkinter import *
obj = Tk()
obj.title("Radio_Button")
obj.geometry('300x300')
v1 = StringVar()


def m1():
    option = "selected option is " + v1.get()
    lb1.config(text=option)


rb1 = Radiobutton(obj, text="yes", variable=v1, value="Yes", command=m1)
rb2 = Radiobutton(obj, text="no", variable=v1, value="No", command=m1)

rb1.pack()
rb2.pack()

lb1 = Label(obj)
lb1.pack()

obj.mainloop()