import tkinter
obj = tkinter.Tk()
obj.title("Flag")
obj.geometry('750x546')

frame1 = tkinter.Frame(obj, bg="orange", width=600, height=100)
frame1.place(x=50, y=50)

frame2 = tkinter.Frame(obj, bg="white", width=600, height=100)
frame2.place(x=50, y=160)

frame3 = tkinter.Frame(obj, bg="green", width=600, height=100)
frame3.place(x=50, y=270)

obj.mainloop()