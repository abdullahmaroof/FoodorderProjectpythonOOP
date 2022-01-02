from tkinter import *
from PIL import ImageTk, Image
from Final_Project.voice_system import voice_burger
from Final_Project.Bill_Data import *
from tkinter import messagebox
from Final_Project.voice_system import voice_bill
import sqlite3
from Final_Project.Billdata_inoracle import bill

def call_burgermenu():

    class call_burger:
        def __init__(self, root):
            self.root = root
            root.geometry("800x650")
            root.title('Online Food Order System')
            root.iconbitmap(r'buy_online_5Wq_icon.ico')
            #*****************upper block*****************************
            upper_Root = Frame(root, bg="light blue", height=100)
            title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial',28,'bold','underline'))

            upper_Root.pack(side=TOP, fill=BOTH, expand=1)
            title.pack(pady=30)


            #*********************Center Block*******************
            center_Root = Frame(root, bg="gray92", height=500)

            #*********top-center*****
            top_center = Frame(center_Root, bg="gray92", height=100)
            self.pic = Image.open("burger.PNG")
            self.resized = self.pic.resize((150, 100), Image.ANTIALIAS)
            self.mypic = ImageTk.PhotoImage(self.resized)
            image_top_center = Label(top_center, image = self.mypic)

            #*********center-center pack*****
            center_center = Frame(root, bg="white", height=420)
            subtitle_frame = Frame(center_center, bg="white", height=50)
            subtitle_label = Label(subtitle_frame, text="Burger Menu", font=('arial',16,'bold','underline'), bg="white")
            #headings
            heading_frame = Frame(center_center, bg="white", height=20)
            name_frame = Frame(heading_frame, bg="white", height=20)
            name_label = Label(name_frame, text="Flavour", font=('arial',12,'bold'), bg="white")
            price_frame = Frame(heading_frame, bg="white", height=20)
            price_label = Label(price_frame, text="Prices", font=('arial',12,'bold'), bg="white")
            bcold_frame = Frame(heading_frame, bg="white", height=20)
            bcold_label = Label(bcold_frame, text="With Drink", font=('arial',12,'bold'), bg="white")
            bcoldf_frame = Frame(heading_frame, bg="white", height=20)
            bcoldf_label = Label(bcoldf_frame, text="With Fries", font=('arial',12,'bold'), bg="white")


            #zinger burger
            zb_frame = Frame(center_center, bg="white", height=50)
            zbname_frame = Frame(zb_frame, bg="white", height=30)
            zbname_label = Label(zbname_frame, text="Zinger Burger", font=('arial',12,'bold'), bg="white")
            zbprice_frame = Frame(zb_frame, bg="white", height=30)
            zbprice_btn = Button(zbprice_frame,  text="400 RS", command = lambda : self.zinburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            zbcold_frame = Frame(zb_frame, bg="white", height=30)
            zbcold_btn = Button(zbcold_frame,  text="500 RS", command = lambda : self.dzinburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            zbcoldf_frame = Frame(zb_frame, bg="white", height=30)
            zbcoldf_btn = Button(zbcoldf_frame,  text="600 RS", command = lambda : self.fzinburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

            #beef burger
            bb_frame = Frame(center_center, bg="white", height=50)
            bbname_frame = Frame(bb_frame, bg="white", height=30)
            bbname_label = Label(bbname_frame, text="Beef    Burger", font=('arial',12,'bold'), bg="white")
            bbprice_frame = Frame(bb_frame, bg="white", height=30)
            bbprice_btn = Button(bbprice_frame,  text="500 RS", command = lambda : self.beefburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            bbcold_frame = Frame(bb_frame, bg="white", height=30)
            bbcold_btn = Button(bbcold_frame,  text="600 RS", command = lambda : self.dbeefburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            bbcoldf_frame = Frame(bb_frame, bg="white", height=30)
            bbcoldf_btn = Button(bbcoldf_frame,  text="700 RS", command = lambda : self.fbeefburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

            #Chicken burger
            cb_frame = Frame(center_center, bg="white", height=50)
            cbname_frame = Frame(cb_frame, bg="white", height=30)
            cbname_label = Label(cbname_frame, text="Chick. Burger", font=('arial',12,'bold'), bg="white")
            cbprice_frame = Frame(cb_frame, bg="white", height=30)
            cbprice_btn = Button(cbprice_frame,  text="450 RS", command = lambda : self.chburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            cbcold_frame = Frame(cb_frame, bg="white", height=30)
            cbcold_btn = Button(cbcold_frame,  text="550 RS", command = lambda : self.dchburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            cbcoldf_frame = Frame(cb_frame, bg="white", height=30)
            cbcoldf_btn = Button(cbcoldf_frame,  text="650 RS", command = lambda : self.fchburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

            #shotgun burger
            sb_frame = Frame(center_center, bg="white", height=50)
            sbname_frame = Frame(sb_frame, bg="white", height=30)
            sbname_label = Label(sbname_frame, text="Shotgun Burg", font=('arial',12,'bold'), bg="white")
            sbprice_frame = Frame(sb_frame, bg="white", height=30)
            sbprice_btn = Button(sbprice_frame,  text="350 RS", command = lambda : self.sgburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            sbcold_frame = Frame(sb_frame, bg="white", height=30)
            sbcold_btn = Button(sbcold_frame,  text="450 RS", command = lambda : self.dsgburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            sbcoldf_frame = Frame(sb_frame, bg="white", height=30)
            sbcoldf_btn = Button(sbcoldf_frame,  text="550 RS", command = lambda : self.fsgburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

            #BBQ burger
            bbb_frame = Frame(center_center, bg="white", height=50)
            bbbname_frame = Frame(bbb_frame, bg="white", height=30)
            bbbname_label = Label(bbbname_frame, text="BarBQ Burger", font=('arial',12,'bold'), bg="white")
            bbbprice_frame = Frame(bbb_frame, bg="white", height=30)
            bbbprice_btn = Button(bbbprice_frame,  text="500 RS", command = lambda : self.bbqburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            bbbcold_frame = Frame(bbb_frame, bg="white", height=30)
            bbbcold_btn = Button(bbbcold_frame,  text="600 RS", command = lambda : self.dbbqburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            bbbcoldf_frame = Frame(bbb_frame, bg="white", height=30)
            bbbcoldf_btn = Button(bbbcoldf_frame,  text="700 RS", command = lambda : self.fbbqburger(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")



            center_Root.pack(side=TOP, fill=BOTH, expand=1)

            #*********top-center pack*****
            top_center.pack(side=TOP, fill=BOTH, expand=1)
            image_top_center.pack(pady=20)


            #********center-center pack*******
            center_center.pack(side=TOP, fill=BOTH, expand=1, pady=10, padx=20)
            subtitle_frame.pack(side=TOP, fill=BOTH, expand=1)
            subtitle_label.pack(pady=10)
            #heading pack
            heading_frame.pack(side=TOP, fill=BOTH, expand=1, padx= 10)
            name_frame.pack(side=LEFT, fill=BOTH, expand=1)
            name_label.pack()
            price_frame.pack(side=LEFT, fill=BOTH, expand=1)
            price_label.pack()
            bcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bcold_label.pack()
            bcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bcoldf_label.pack()

            #zinger pack
            zb_frame.pack(side=TOP, fill=BOTH, expand=1)
            zbname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            zbname_label.pack(pady=10)
            zbprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            zbprice_btn.pack(pady=10)
            zbcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            zbcold_btn.pack(pady=10)
            zbcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            zbcoldf_btn.pack(pady=10)

            #beef pack
            bb_frame.pack(side=TOP, fill=BOTH, expand=1)
            bbname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbname_label.pack(pady=10)
            bbprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbprice_btn.pack(pady=10)
            bbcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbcold_btn.pack(pady=10)
            bbcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbcoldf_btn.pack(pady=10)


            #chicken pack
            cb_frame.pack(side=TOP, fill=BOTH, expand=1)
            cbname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            cbname_label.pack(pady=10)
            cbprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            cbprice_btn.pack(pady=10)
            cbcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            cbcold_btn.pack(pady=10)
            cbcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            cbcoldf_btn.pack(pady=10)


            #shotgun pack
            sb_frame.pack(side=TOP, fill=BOTH, expand=1)
            sbname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            sbname_label.pack(pady=10)
            sbprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            sbprice_btn.pack(pady=10)
            sbcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            sbcold_btn.pack(pady=10)
            sbcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            sbcoldf_btn.pack(pady=10)


            #BBQ pack
            bbb_frame.pack(side=TOP, fill=BOTH, expand=1)
            bbbname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbbname_label.pack(pady=10)
            bbbprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbbprice_btn.pack(pady=10)
            bbbcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbbcold_btn.pack(pady=10)
            bbbcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbbcoldf_btn.pack(pady=10)


            #*****************bottom block*****************************
            bottom_Root = Frame(root, bg="light blue", height=50)
            copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof & Zubair Ali 2020", bg="light blue", font=('arial',12,'bold'))

            bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
            copyRight.pack()

        def zinburger(self):
            self.data = burger_zinger
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def dzinburger(self):
            self.data = dburger_zinger
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def fzinburger(self):
            self.data = fburger_zinger
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def beefburger(self):
            self.data = burger_beef
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def dbeefburger(self):
            self.data = dburger_beef
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def fbeefburger(self):
            self.data = fburger_beef
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def chburger(self):
            self.data = burger_chicken
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def dchburger(self):
            self.data = dburger_chicken
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def fchburger(self):
            self.data = fburger_chicken
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def sgburger(self):
            self.data = burger_shotgun
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def dsgburger(self):
            self.data = dburger_shotgun
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def fsgburger(self):
            self.data = fburger_shotgun
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def bbqburger(self):
            self.data = burger_bbq
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def dbbqburger(self):
            self.data = dburger_bbq
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

        def fbbqburger(self):
            self.data = fburger_bbq
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = sqlite3.connect("BillRecord.db")
                cursor = con.cursor()
                sql = "INSERT INTO bill VALUES ('" + str(
                    self.billno) + "','" + self.food + "','" + self.flavour + "','" + self.serve + "','" + str(
                    self.price) + "')"
                cursor.execute(sql)
                con.commit()
                con.close()
                messagebox.showinfo("Order", "\t\tBill # " + str(
                    self.billno) + "       \n  Food: " + self.food + "\n  Flavour: " + self.flavour + "\n  Serve with: " + self.serve + "\n  Price " + str(
                    self.price) + "\n  " + self.message, parent=self.root)
                bill(str(self.billno), self.food, self.flavour, self.serve, self.price)
            except Exception as es:
                messagebox.showerror("Error", f"Error due to {str(es)}", parent=self.root)

    root = Toplevel()
    obj = call_burger(root)
    voice_burger.wishme()
    mainloop()