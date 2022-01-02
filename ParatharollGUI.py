from tkinter import *
from PIL import ImageTk, Image
from VoiceSystem import voice_paratharoll
from tkinter import messagebox
from VoiceSystem import voice_bill
import sqlite3
from Final_Project.Bill_Data import *
from Final_Project.Billdata_inoracle import bill

def call_parathamenu():
    class call_paratharoll:
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
            self.pic = Image.open("paratharoll.PNG")
            self.resized = self.pic.resize((150, 100), Image.ANTIALIAS)
            self.mypic = ImageTk.PhotoImage(self.resized)
            image_top_center = Label(top_center, image=self.mypic)

            #*********center-center pack*****
            center_center = Frame(root, bg="white", height=420)
            subtitle_frame = Frame(center_center, bg="white", height=50)
            subtitle_label = Label(subtitle_frame, text="Paratharoll Menu", font=('arial',16,'bold','underline'), bg="white")
            #headings
            heading_frame = Frame(center_center, bg="white", height=20)
            name_frame = Frame(heading_frame, bg="white", height=20)
            name_label = Label(name_frame, text="Flavour", font=('arial',12,'bold'), bg="white")
            price_frame = Frame(heading_frame, bg="white", height=20)
            price_label = Label(price_frame, text="Prices", font=('arial',12,'bold'), bg="white")
            pcold_frame = Frame(heading_frame, bg="white", height=20)
            pcold_label = Label(pcold_frame, text="With Drink", font=('arial',12,'bold'), bg="white")
            pcoldf_frame = Frame(heading_frame, bg="white", height=20)
            pcoldf_label = Label(pcoldf_frame, text="With Fries", font=('arial',12,'bold'), bg="white")


            #zinger paratharoll
            zp_frame = Frame(center_center, bg="white", height=50)
            zpname_frame = Frame(zp_frame, bg="white", height=30)
            zpname_label = Label(zpname_frame, text="Zinger Paratha", font=('arial',12,'bold'), bg="white")
            zpprice_frame = Frame(zp_frame, bg="white", height=30)
            zpprice_btn = Button(zpprice_frame,  text="500 RS", command = lambda : self.zinparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            zpcold_frame = Frame(zp_frame, bg="white", height=30)
            zpcold_btn = Button(zpcold_frame,  text="550 RS", command = lambda : self.dzinparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            zpcoldf_frame = Frame(zp_frame, bg="white", height=30)
            zpcoldf_btn = Button(zpcoldf_frame,  text="600 RS", command = lambda : self.fzinparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

            #beef paratharoll
            bp_frame = Frame(center_center, bg="white", height=50)
            bpname_frame = Frame(bp_frame, bg="white", height=30)
            bpname_label = Label(bpname_frame, text="Beef    Paratha", font=('arial',12,'bold'), bg="white")
            bpprice_frame = Frame(bp_frame, bg="white", height=30)
            bpprice_btn = Button(bpprice_frame,  text="600 RS", command = lambda : self.beefparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            bpcold_frame = Frame(bp_frame, bg="white", height=30)
            bpcold_btn = Button(bpcold_frame,  text="650 RS", command = lambda : self.dbeefparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            bpcoldf_frame = Frame(bp_frame, bg="white", height=30)
            bpcoldf_btn = Button(bpcoldf_frame,  text="700 RS", command = lambda : self.fbeefparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

            #Chicken burger
            cp_frame = Frame(center_center, bg="white", height=50)
            cpname_frame = Frame(cp_frame, bg="white", height=30)
            cpname_label = Label(cpname_frame, text="Chicken Para.", font=('arial',12,'bold'), bg="white")
            cpprice_frame = Frame(cp_frame, bg="white", height=30)
            cpprice_btn = Button(cpprice_frame,  text="450 RS", command = lambda : self.chparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            cpcold_frame = Frame(cp_frame, bg="white", height=30)
            cpcold_btn = Button(cpcold_frame,  text="500 RS", command = lambda : self.dchparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            cpcoldf_frame = Frame(cp_frame, bg="white", height=30)
            cpcoldf_btn = Button(cpcoldf_frame,  text="550 RS", command = lambda : self.fchparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

            #Smoke paratha roll
            sp_frame = Frame(center_center, bg="white", height=50)
            spname_frame = Frame(sp_frame, bg="white", height=30)
            spname_label = Label(spname_frame, text="SmokePartha", font=('arial',12,'bold'), bg="white")
            spprice_frame = Frame(sp_frame, bg="white", height=30)
            spprice_btn = Button(spprice_frame,  text="600 RS", width=15, command = lambda : self.sparatha(), bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            spcold_frame = Frame(sp_frame, bg="white", height=30)
            spcold_btn = Button(spcold_frame,  text="650 RS", command = lambda : self.dsparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            spcoldf_frame = Frame(sp_frame, bg="white", height=30)
            spcoldf_btn = Button(spcoldf_frame,  text="700 RS", command = lambda : self.fsparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

            #BBQ paratha
            bbp_frame = Frame(center_center, bg="white", height=50)
            bbpname_frame = Frame(bbp_frame, bg="white", height=30)
            bbpname_label = Label(bbpname_frame, text="BBQ Paratha", font=('arial',12,'bold'), bg="white")
            bbpprice_frame = Frame(bbp_frame, bg="white", height=30)
            bbpprice_btn = Button(bbpprice_frame,  text="500 RS", command = lambda : self.bbqparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            bbpcold_frame = Frame(bbp_frame, bg="white", height=30)
            bbpcold_btn = Button(bbpcold_frame,  text="600 RS", width=15, command = lambda : self.dbbqparatha(), bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            bbpcoldf_frame = Frame(bbp_frame, bg="white", height=30)
            bbpcoldf_btn = Button(bbpcoldf_frame,  text="700 RS", command = lambda : self.fbbqparatha(), width=15, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")



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
            pcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            pcold_label.pack()
            pcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            pcoldf_label.pack()

            #zinger pack
            zp_frame.pack(side=TOP, fill=BOTH, expand=1)
            zpname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            zpname_label.pack(pady=10)
            zpprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            zpprice_btn.pack(pady=10)
            zpcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            zpcold_btn.pack(pady=10)
            zpcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            zpcoldf_btn.pack(pady=10)

            #beef pack
            bp_frame.pack(side=TOP, fill=BOTH, expand=1)
            bpname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bpname_label.pack(pady=10)
            bpprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bpprice_btn.pack(pady=10)
            bpcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bpcold_btn.pack(pady=10)
            bpcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bpcoldf_btn.pack(pady=10)


            #chicken pack
            cp_frame.pack(side=TOP, fill=BOTH, expand=1)
            cpname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            cpname_label.pack(pady=10)
            cpprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            cpprice_btn.pack(pady=10)
            cpcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            cpcold_btn.pack(pady=10)
            cpcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            cpcoldf_btn.pack(pady=10)


            #shotgun pack
            sp_frame.pack(side=TOP, fill=BOTH, expand=1)
            spname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            spname_label.pack(pady=10)
            spprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            spprice_btn.pack(pady=10)
            spcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            spcold_btn.pack(pady=10)
            spcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            spcoldf_btn.pack(pady=10)


            #BBQ pack
            bbp_frame.pack(side=TOP, fill=BOTH, expand=1)
            bbpname_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbpname_label.pack(pady=10)
            bbpprice_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbpprice_btn.pack(pady=10)
            bbpcold_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbpcold_btn.pack(pady=10)
            bbpcoldf_frame.pack(side=LEFT, fill=BOTH, expand=1)
            bbpcoldf_btn.pack(pady=10)


            #*****************bottom block*****************************
            bottom_Root = Frame(root, bg="light blue", height=50)
            copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof & Zubair Ali 2020", bg="light blue", font=('arial',12,'bold'))

            bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
            copyRight.pack()

        def zinparatha(self):
            self.data = parroll_zinger
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = connect("BillRecord.db")
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

        def dzinparatha(self):
            self.data = dparroll_zinger
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = connect("BillRecord.db")
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

        def fzinparatha(self):
            self.data = fparroll_zinger
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = connect("BillRecord.db")
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

        def beefparatha(self):
            self.data = parroll_beef
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = connect("BillRecord.db")
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

        def dbeefparatha(self):
            self.data = dparroll_beef
            self.billno = self.data.rand_value
            self.food = self.data.food
            self.flavour = self.data.flavour
            self.serve = self.data.servewith
            self.price = self.data.price
            self.message = self.data.note
            voice_bill.wishme()
            try:
                con = connect("BillRecord.db")
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

        def fbeefparatha(self):
            self.data = fparroll_beef
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

        def chparatha(self):
            self.data = parroll_chicken
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

        def dchparatha(self):
            self.data = dparroll_chicken
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

        def fchparatha(self):
            self.data = fparroll_chicken
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

        def sparatha(self):
            self.data = parroll_smoke
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

        def dsparatha(self):
            self.data = dparroll_smoke
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

        def fsparatha(self):
            self.data = fparroll_smoke
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

        def bbqparatha(self):
            self.data = parroll_bbq
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

        def dbbqparatha(self):
            self.data = dparroll_bbq
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

        def fbbqparatha(self):
            self.data = fparroll_bbq
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
    obj = call_paratharoll(root)
    voice_paratharoll.wishme()
    mainloop()