from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Management Sysytem")
        self.root.geometry("1550x800+0+0")
        labeltitle = Label(self.root, text="PHARMACY MANAGEMENT SYSTEM", bd=15, relief=RIDGE,
                           bg='white', fg='darkgreen', font=("times new roman", 50, 'bold'), padx=2, pady=4)

        labeltitle.pack(side=TOP, fill=X)
        img1 = Image.open("./logo.jpg")
        img1 = img1.resize((80, 80), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=70, y=17)

        Dataframe = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        Dataframe.place(x=0, y=120, width=1530, height=350)
        Dataframeleft = LabelFrame(Dataframe, text="Medicine Information",
                                   bd=10, relief=RIDGE, fg="dark green", font=("arial", 15, 'bold'))
        Dataframeleft.place(x=0, y=5, width=900, height=300)
        DataframeRight = LabelFrame(Dataframe, text="Medicine Add Department",
                                    bd=10, relief=RIDGE, fg="dark green", font=("arial", 15, 'bold'))
        DataframeRight.place(x=910, y=5, width=550, height=300)

        Buttonframe = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        Buttonframe.place(x=0, y=475, width=1530, height=65)

        btnAddData = Button(Buttonframe, text="Add Medicine", font=(
            "arial", 15, 'bold'), bg="dark green", fg="white")
        btnAddData.grid(row=0, column=0)
        btnupdateData = Button(Buttonframe, text="Update", width=12, font=(
            "arial", 15, 'bold'), bg="dark green", fg="white")
        btnupdateData.grid(row=0, column=1)
        btndelData = Button(Buttonframe, text="Delete", width=12, font=(
            "arial", 15, 'bold'), bg="red", fg="white")
        btndelData.grid(row=0, column=2)
        btnresetData = Button(Buttonframe, text="Reset", width=12, font=(
            "arial", 15, 'bold'), bg="dark green", fg="white")
        btnresetData.grid(row=0, column=3)
        btnexitData = Button(Buttonframe, text="Exit", width=12, font=(
            "arial", 15, 'bold'), bg="dark green", fg="white")
        btnexitData.grid(row=0, column=4)

        lblSearch = Label(Buttonframe, font=("arial", 17, "bold"),
                          text="Search", width=5, padx=10, bg="black", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        search_combo = ttk.Combobox(Buttonframe, width=12, font=(
            "arial", 17, "bold"), state='readonly')
        search_combo["values"] = ("Reference", "Med name", "Lot number")
        search_combo.grid(row=0, column=6)
        search_combo.current(0)

        txtsearch = Entry(Buttonframe, bd=3, relief=RIDGE,
                          width=12, font=("arial", 15, "bold"))
        txtsearch.grid(row=0, column=7)

        btnsearchData = Button(Buttonframe, text="Search", width=12, font=(
            "arial", 15, 'bold'), bg="dark green", fg="white")
        btnsearchData.grid(row=0, column=8)
        btnshowData = Button(Buttonframe, text="Show All", width=12, font=(
            "arial", 15, 'bold'), bg="dark green", fg="white")
        btnshowData.grid(row=0, column=9)

        lblrefnum = Label(Dataframeleft, text="Reference No.", font=(
            "arial", 15, "bold"), width=12, fg="black", padx=2)
        lblrefnum.grid(row=0, column=0, sticky=W)
        txtrefnum = Entry(Dataframeleft, bd=3, font=(
            "arial", 10, "bold"), width=29, relief=RIDGE)
        txtrefnum.grid(row=0, column=1)

        lblcomname = Label(Dataframeleft, text="Company name:", font=(
            "arial", 15, "bold"), width=12, fg="black", padx=5)
        txtcomname = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblcomname.grid(row=1, column=0, sticky=W)
        txtcomname.grid(row=1, column=1)

        lbltype = Label(Dataframeleft, text="Type Of Medicine", font=(
            "arial", 15, "bold"), width=13, fg="black", padx=2)
        lbltype.grid(row=2, column=0, sticky=W)

        type_combo = ttk.Combobox(
            Dataframeleft, width=27, font=("arial", 10, "bold"))
        type_combo["values"] = ("Tablet", "Injection",
                                "Syrup", "Capsule", "Equipments")
        type_combo.grid(row=2, column=1)

        lblmedname = Label(Dataframeleft, text="Medicine Name", font=(
            "arial", 15, "bold"), width=12, fg="black", padx=2)
        lblmedname.grid(row=3, column=0, sticky=W)

        med_combo = ttk.Combobox(
            Dataframeleft, width=27, font=("arial", 10, "bold"))
        med_combo["values"] = ("crocin", "omnigel")
        med_combo.grid(row=3, column=1)

        lbllotnum = Label(Dataframeleft, text="Lot No.  :", font=(
            "arial", 15, "bold"), width=7, fg="black", padx=5)
        txtlotnum = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lbllotnum.grid(row=4, column=0, sticky=W)
        txtlotnum.grid(row=4, column=1)

        lblIssueDate = Label(Dataframeleft, text="Issue Date :", font=(
            "arial", 15, "bold"), width=10, fg="black", padx=2)
        txtIssueDate = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(Dataframeleft, text="Expiry Date :", font=(
            "arial", 15, "bold"), width=10, fg="black", padx=2)
        txtExpDate = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate.grid(row=6, column=1)

        lbluses = Label(Dataframeleft, text="Uses", font=(
            "arial", 15, "bold"), width=5, fg="black", padx=2)
        txtuses = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lbluses.grid(row=7, column=0, sticky=W)
        txtuses.grid(row=7, column=1)

        lblSideeffects = Label(Dataframeleft, text="Side Effects", font=(
            "arial", 15, "bold"), width=10, fg="black", padx=2)
        txtSideeffects = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblSideeffects.grid(row=8, column=0, sticky=W)
        txtSideeffects.grid(row=8, column=1)

        lblDosage = Label(Dataframeleft, text="Dosage :", font=(
            "arial", 15, "bold"), width=12, fg="black", padx=2)
        txtDosage = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblDosage.grid(row=0, column=4, sticky=W)
        txtDosage.grid(row=0, column=5)

        lblprice = Label(Dataframeleft, text="Tablets Price :", font=(
            "arial", 15, "bold"), width=12, fg="black", padx=2)
        txtprice = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblprice.grid(row=1, column=4, sticky=W)
        txtprice.grid(row=1, column=5)

        lblquantity = Label(Dataframeleft, text="Tablets Qty :", font=(
            "arial", 15, "bold"), width=12, fg="black", padx=2)
        txtquantity = Entry(Dataframeleft, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        lblquantity.grid(row=2, column=4, sticky=W)
        txtquantity.grid(row=2, column=5)

        img2 = Image.open("./download.jpg")
        img2 = img2.resize((250, 150), Image.ANTIALIAS)
        self.img2 = ImageTk.PhotoImage(img2)
        b2 = Button(self.root, image=self.img2, borderwidth=0)
        b2.place(x=450, y=270)

        img3 = Image.open("./pic1.jpg")
        img3 = img3.resize((250, 150), Image.ANTIALIAS)
        self.img3 = ImageTk.PhotoImage(img3)
        b3 = Button(self.root, image=self.img3, borderwidth=0)
        b3.place(x=670, y=270)

        img4 = Image.open("./pic2.jpg")
        img4 = img4.resize((350, 50), Image.ANTIALIAS)
        self.img4 = ImageTk.PhotoImage(img4)
        b4 = Button(self.root, image=self.img4, borderwidth=0)
        b4.place(x=970, y=175)

        img5 = Image.open("./pic1.jpg")
        img5 = img5.resize((150, 150), Image.ANTIALIAS)
        self.img5 = ImageTk.PhotoImage(img5)
        b3 = Button(self.root, image=self.img5, borderwidth=0)
        b3.place(x=1320, y=165)

        lblref1 = Label(DataframeRight, text="Reference No. :", font=(
            "arial", 12, "bold"), width=12, fg="black", padx=2)
        lblref1.place(x=0, y=80)
        txtref1 = Entry(DataframeRight, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        txtref1.place(x=135, y=80)

        lblmed1 = Label(DataframeRight, text="Medicine Name :", font=(
            "arial", 12, "bold"), width=12, fg="black", padx=2)
        lblmed1.place(x=0, y=110)
        txtmed1 = Entry(DataframeRight, width=29, font=(
            "arial", 10, "bold"), bd=3, relief=RIDGE)
        txtmed1.place(x=135, y=110)

        side_frame = Frame(DataframeRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=0, y=150, width=290, height=110)

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(
            side_frame, xscrollcommand=sc_x.set, yscrollcommand=sc_y.set, column=("Ref", "Med name"))

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("Ref", text="Ref")
        self.medicine_table.heading("Med name", text="MedName")

        self.medicine_table["show"] = ("headings")
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("Ref", width=100)
        self.medicine_table.column("Med name", width=100)

        down_frame=Frame(DataframeRight,bd=4,relief=RIDGE,bg="white")
        down_frame.place(x=370,y=150,width=135,height=115)
        
        btnAddmed=Button(down_frame,text="ADD",font=("arial",8,"bold"),width=12,bg="lime",fg="black",pady=2)
        btnAddmed.grid(row=0,column=0)

        btnupdatemed=Button(down_frame,text="UPDATE",font=("arial",8,"bold"),width=12,bg="blue",fg="black",pady=2)
        btnupdatemed.grid(row=1,column=0)

        btndelmed=Button(down_frame,text="DELETE",font=("arial",8,"bold"),width=12,bg="red",fg="black",pady=2)
        btndelmed.grid(row=2,column=0)

        btnclrmed=Button(down_frame,text="CLEAR",font=("arial",8,"bold"),width=12,bg="orange",fg="black",pady=2)
        btnclrmed.grid(row=3,column=0)

        frame_details=Frame(self.root,bd=15,relief=RIDGE)
        frame_details.place(x=0,y=537,width=1530,height=240)



    


if __name__ == '__main__':
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
