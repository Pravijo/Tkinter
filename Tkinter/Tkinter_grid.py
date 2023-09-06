import tkinter
obj = tkinter.Tk()
obj.geometry('400x400')
obj.title("Registration Form")
tkinter.Label(obj, text="Registration Form", font=("ariel", 24, "bold")).grid(row=0, column=2)

tkinter.Label(obj, text="Full Name").grid(row=2, column=1)
tkinter.Entry(obj).grid(row=2, column=2)
tkinter.Label(obj, text="Last Name").grid(row=6, column=1)
tkinter.Entry(obj).grid(row=6, column=2)
tkinter.Label(obj, text="Email address").grid(row=8,column=1)
tkinter.Entry(obj).grid(row=8, column=2)
tkinter.Label(obj, text="Email address").grid(row=8,column=1)
tkinter.Entry(obj).grid(row=8, column=2)
tkinter.Label(obj, text="password").grid(row=10,column=1)
tkinter.Entry(obj).grid(row=10, column=2)


tkinter.Button(obj, text="Create", fg="blue", bg="grey").grid(row=14, column=1)
tkinter.Button(obj, text="Signup", fg="blue", bg="grey").grid(row=14, column=2)

obj.mainloop()



