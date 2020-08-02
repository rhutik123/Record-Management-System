from tkinter import *
from tkinter import messagebox

class login:
    def __init__(self, root):
        self.root=root
        self.root.title("Rhutik's record management system")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg='#1287A5')

        F1 = Frame(self.root,bd=10,relief=GROOVE,bg='#45CE30')
        F1.place(x=450,y=150,height=350)

        self.user = StringVar()
        self.password = StringVar()


        title= Label(F1,text="Admin login", font=("monospace", 30, "bold"),bg='#45CE30').grid(row=0,columnspan=2,pady=20)
        lblusername = Label(F1,text="Username",font=("monospace", 25, "bold"),bg='#45CE30').grid(row=1,column=0,pady=10,padx=10)

        txtuser = Entry(F1, bd=7, relief=GROOVE,textvariable=self.user , width=25,font="monospace 15 bold").grid(row=1,column=1,padx=10,pady=10)

        lblpass = Label(F1,text="Password", font=("monospace", 25, "bold"),bg='#45CE30').grid(row=2,column=0,pady=10,padx=10)
        txtpass = Entry(F1, bd=7, relief=GROOVE,show="*",textvariable=self.password ,width=25,font="monospace 15 bold").grid(row=2,column=1,padx=10,pady=10)

        btnlog = Button(F1, text="Login", bd=7, width=10,font=("monospace 15 bold"),command=self.logfun,bg='#74B9FF').place(x=10,y=250)
        btnreset = Button(F1, text="Reset", bd=7,width=10,font=("monospace 15 bold"), command=self.reset,bg='#74B9FF').place(x=180,y=250)
        btnexit = Button(F1, text="Exit", bd=7,width=10,font=("monospace 15 bold"),command=self.exit,bg='#74B9FF').place(x=350,y=250)

    def logfun(self):
        if self.user.get()=="rhutik" and self.password.get()=="rhutik.123":
            self.root.destroy()
            import software
            software.File_app()
        else:
            messagebox.showerror("Error", "Invalid username or password")
            self.user.set("")
            self.password.set("")

    def reset(self):
        self.user.set("")
        self.password.set("")

    def exit(self):
        option=messagebox.askyesno("Exit", "Do yoy really want to exit?")
        if option > 0:
            self.root.destroy()
        else:
            return

root=Tk()
ob=login(root)
root.mainloop()