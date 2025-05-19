import tkinter as tk
app = tk.Tk()
app.title = ("SIGN IN")

logo = tk.PhotoImage(file="rfapp.png")

app.geometry = ('1000x1000')
tk.Label(app,text = "Enter your Name").grid(row=0,column=0)
tk.Entry(app).grid(row=0,column=1)
tk.Button(app,text = "submit").grid(row=2,column=0)


tk.Label(app,text = "Your password").grid(column=0,row=1)
tk.Entry(app).grid(column=1,row=1)
verifybutton = tk.Button(app,text = "verify here please" , bg='blue',
                         padx=10, pady=10).grid(column=1,row=2)

app.mainloop()

