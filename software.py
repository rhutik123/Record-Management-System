from tkinter import *
from tkinter import ttk, messagebox
import os

class File_app():
    def __init__(self):
        self.root = Tk()
        self.root.title("Record management system")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg='#2ecc72')


        title = Label(self.root, text="Record management system", bd=10,relief=GROOVE,font=("monospace", 35,"bold"),bg="yellow",fg='red')
        title.pack(fill=X)

        employer_frame = Frame(self.root, bd=10, relief=GROOVE,bg="#01CBC6")
        employer_frame.place(x=10,y=100,height=480)

        # all veriable ################
        self.e_id = StringVar()
        self.contact = StringVar()
        self.name = StringVar()
        self.date = StringVar()
        self.course = StringVar()
        self.degree = StringVar()
        self.address = StringVar()
        self.proof = StringVar()
        self.country = StringVar()
        self.payment = StringVar()

        emp_fram_title = Label(employer_frame,text="Employer details", font=("monospace", 25,"bold"),bg="#01CBC6").grid(row = 0, columnspan= 4)

        emp_id = Label(employer_frame, text="Employer ID ", font=("monospace", 17,"bold"),bg="#01CBC6").grid(row=1, column=0,pady=25, padx=15,sticky="w")
        id_entry = Entry(employer_frame,width=18, bd=7, textvariable=self.e_id,relief=GROOVE,font="monospace 15 bold").grid(row=1, column=1)

        emp_contact = Label(employer_frame,text="Contact No. ", font=("monospace", 17, "bold"),bg="#01CBC6").grid(row=1,column=2,pady=25, padx=15,sticky="w")
        contact_entry = Entry(employer_frame,width=18, bd=7, textvariable=self.contact,relief=GROOVE,font="monospace 15 bold").grid(row=1, column=3)
        
        emp_name = Label(employer_frame, text="Employer Name ", font=("monospace", 17, "bold"),bg="#01CBC6").grid(row=2, column=0,pady=25, padx=15,sticky="w")
        name_entry = Entry(employer_frame,width=18, bd=7, textvariable=self.name,relief=GROOVE,font="monospace 15 bold").grid(row=2, column=1)

        emp_date = Label(employer_frame, text="DoB(dd/mm/yyyy)", font=("monospace", 17, "bold"),bg="#01CBC6").grid(row=2,column=2,pady=25, padx=15,sticky="w")
        date_entry = Entry(employer_frame,width=18, bd=7, textvariable=self.date,relief=GROOVE,font="monospace 15 bold").grid(row=2, column=3)

        emp_course = Label(employer_frame, text="Course", font=("monospace", 17,"bold"),bg="#01CBC6").grid(row=3,column=0,pady=25, padx=15,sticky="w")
        course_entry = Entry(employer_frame,width=18, bd=7, textvariable=self.course,relief=GROOVE,font="monospace 15 bold").grid(row=3, column=1)

        emp_degree = Label(employer_frame, text="Select degree", font=("monospace", 17,"bold"),bg="#01CBC6").grid(row=3,column=2,pady=25, padx=15,sticky="w")
        degree_combo = ttk.Combobox(employer_frame, width = 15, state = "readonly", textvariable=self.degree,font=("monospace 15 bold"))
        degree_combo['values'] = ("B.Tech","M.Tech", "12th Pass", "P.hd", "deploma", "Computer Science", "Other")
        degree_combo.grid(row=3, column=3)

        emp_address = Label(employer_frame, text="Address", font=("monospace", 17,"bold"),bg="#01CBC6").grid(row=4,column=0,pady=25, padx=15,sticky="w")
        address_entry = Entry(employer_frame,width=18, bd=7,textvariable=self.address, relief=GROOVE,font="monospace 15 bold").grid(row=4, column=1)
        
        emp_proof = Label(employer_frame, text="ID Proof", font=("monospace", 17,"bold"),bg="#01CBC6").grid(row=4,column=2,pady=25, padx=15,sticky="w")
        proof_combo = ttk.Combobox(employer_frame, width = 18, state = "readonly", textvariable=self.proof,font=("monospace 15 bold"))
        proof_combo['values'] = ("Adhaar Card","Pan card", "Passport", "Voter card", "Driving licence", "Other")
        proof_combo.grid(row=4, column=3)

        emp_country = Label(employer_frame, text="country", font=("monospace", 17,"bold"),bg="#01CBC6").grid(row=5,column=0,pady=25, padx=15,sticky="w")
        country_entry = Entry(employer_frame,width=18, bd=7, textvariable=self.country,relief=GROOVE,font="monospace 15 bold").grid(row=5, column=1)

        emp_payment = Label(employer_frame, text="Payment Mode", font=("monospace", 17,"bold"),bg="#01CBC6").grid(row=5,column=2,pady=25, padx=15,sticky="w")
        payment_combo = ttk.Combobox(employer_frame, width = 18, state = "readonly", textvariable=self.payment,font=("monospace 15 bold"))
        payment_combo['values'] = ("Cash","Net Banking", "Credit/Debit Card", "Paytm", "Paypal", "Master card","BHIM UPI")
        payment_combo.grid(row=5, column=3)        

        btn_frame = Frame(self.root, bd=10, relief=GROOVE,bg="#01CBC6")
        btn_frame.place(x=10, y=600)

        btn_save = Button(btn_frame, text= "Save", font=("monospace",15,"bold"),bg='#53E0BC', command=self.save_data, width=13,bd=7, relief=RAISED).grid(row=0,column=0, padx=35, pady=10)
        btn_delete = Button(btn_frame, text= "Delete", font=("monospace",15,"bold"),bg='#53E0BC', command=self.delete, width=13,bd=7, relief=RAISED).grid(row=0,column=1, padx=35, pady=10)
        btn_clear = Button(btn_frame, text= "Clear", font=("monospace",15,"bold"),bg='#53E0BC', command=self.clear, width=13,bd=7, relief=RAISED).grid(row=0,column=2, padx=35, pady=10)
        btn_logout = Button(btn_frame, text= "Logout", font=("monospace",15,"bold"), command=self.logout,bg='#53E0BC', width=13,bd=7, relief=RAISED).grid(row=0,column=3, padx=35, pady=10)
        btn_exit = Button(btn_frame, text= "Exit", font=("monospace",15,"bold"),bg='#53E0BC', command=self.exit, width=13,bd=7, relief=RAISED).grid(row=0,column=4, padx=35, pady=10)

        file_frame = Frame(self.root, bd=10, relief=GROOVE)
        file_frame.place(x=1000, y=100, width=350, height=480)

        file_lbl = Label(file_frame,text="ALL RECORDS", font=("monospace", 15,"bold"), bg="yellow",fg="red",bd=7,relief=GROOVE).pack(fill=X)

        scroll_y = Scrollbar(file_frame,orient=VERTICAL)
        self.file_list = Listbox(file_frame, bg='#F5BCBA',yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.file_list.yview)
        self.file_list.bind("<ButtonRelease-1>",self.get_data)
        self.file_list.pack(fill=BOTH,expand=1)
        self.show_files()

        self.root.mainloop()

    def save_data(self):
        if self.e_id.get() == "":
            messagebox.showerror("Error","Employer ID is required !!")
        else:
            f = open("records/"+str(self.e_id.get())+".txt","w")
            f.write(
                str(self.e_id.get())+"|"+
                str(self.contact.get())+"|"+
                str(self.name.get())+"|"+
                str(self.date.get())+"|"+
                str(self.course.get())+"|"+
                str(self.degree.get())+"|"+
                str(self.address.get())+"|"+
                str(self.proof.get())+"|"+
                str(self.country.get())+"|"+
                str(self.payment.get())
                    )
            f.close()
            self.show_files()
            messagebox.showinfo("Sucess","Record has been saved successfully")

    def show_files(self):
        files = os.listdir("records/")
        self.file_list.delete(0,END)
        if len(files) > 0:
            for file in files:
                self.file_list.insert(END,file)
    
    def get_data(self,event):
        cursor = self.file_list.curselection()
        f1 = open("records/"+self.file_list.get(cursor))
        values = []
        for f in f1:
            values = f.split('|')
        
        self.e_id.set(values[0])
        self.contact.set(values[1])
        self.name.set(values[2])
        self.date.set(values[3])
        self.course.set(values[4])
        self.degree.set(values[5])
        self.address.set(values[6])
        self.proof.set(values[7])
        self.country.set(values[8])
        self.payment.set(values[9])

    def clear(self):
        self.e_id.set("")
        self.contact.set("")
        self.name.set("")
        self.date.set("")
        self.course.set("")
        self.degree.set("")
        self.address.set("")
        self.proof.set("")
        self.country.set("")
        self.payment.set("")

    def delete(self):
        if self.e_id.get() == "":
            messagebox.showerror("Error", "Employer ID is required")
        else:
            ask = messagebox.askyesno("Delete","Do you really want to delete record?")
            if ask > 0:
                os.remove("records/"+str(self.e_id.get())+".txt")
                self.show_files()
            
    def exit(self):
        ask = messagebox.askyesno("Exit","Do you want to exit?\nplease save if you made any changes")
        if ask > 0:
            self.root.destroy()

    def logout(self):
        ask = messagebox.askyesno("Logout", "Do you want to logout?")
        if ask > 0:
            self.root.destroy()
            import login