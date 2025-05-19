import tkinter as tk
from tkinter import messagebox
app = tk.Tk()
app.title = ("SIGN IN")


app.geometry = ('1000x1000')
tk.Label(app,text = "Enter your Name").grid(row=0,column=0)
tk.Entry(app).grid(row=0,column=1)
tk.Button(app,text = "submit").grid(row=2,column=0)


tk.Label(app,text = "Your password").grid(column=0,row=1)
tk.Entry(app).grid(column=1,row=1)
verifybutton = tk.Button(app,text = "verify here please" , bg='blue',
                         padx=10, pady=10).grid(column=1,row=2)
#messagebox.verifybutton("information","submitting this work is key and sometimes essential to our work")

messagebox.showinfo("information","Note This")
messagebox.showwarning("warning","Making apps is sometimes hard and stressing so mind supporting for this piece of work")
app.mainloop()


