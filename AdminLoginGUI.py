from tkinter import *
from PIL import ImageTk, Image
from Final_Project.voice_system import voice_loginadmin
from Final_Project.system_admin import call_adminsys
from tkinter import messagebox

def call_adminlogin():
    class get_admin():
        def __init__(self, root):
            self.root = root


            root.geometry("800x520")
            root.title('Online Food Order System')
            root.iconbitmap(r'buy_online_5Wq_icon.ico')
            #*****************upper block*****************************
            upper_Root = Frame(root, bg="light blue", height=100)
            title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial',28,'bold','underline'))

            upper_Root.pack(side=TOP, fill=BOTH, expand=1)
            title.pack(pady=30)

            #*****************center block*****************************
            center_Root = Frame(root, bg="gray92", height=400)
            top_center = Frame(center_Root, bg="gray92", height=140)
            self.pic = Image.open("shopping-bag.png")
            self.resized = self.pic.resize((150, 100), Image.ANTIALIAS)
            self.mypic = ImageTk.PhotoImage(self.resized)
            image_top_center = Label(top_center, image = self.mypic)
            center_center = Frame(center_Root, bg="gray92", height=80)
            sub_title = Label(center_center, text="Welcome Admin", bg="gray92", font=('arial',20,'underline','bold'))
            bottom_center = Frame(center_Root, bg="gray92", height=180)
            top_botcenter = Frame(bottom_center, bg="gray92", height=100)
            left_top_bot = Frame(top_botcenter, height=100, bg="gray92")
            name_label = Label(left_top_bot, text="User Name:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
            pass_label = Label(left_top_bot, text="Password:  ", font=('arial',12,'bold'), anchor=E, bg="gray92")
            right_top_bot = Frame(top_botcenter, height=100, bg="gray92")
            top_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
            bottom_right_top_bot = Frame(right_top_bot, height=50, bg="gray92")
            self.name_box = Entry(top_right_top_bot, width=25)
            self.pass_box = Entry(bottom_right_top_bot, width=25)
            bottom_botcenter = Frame(bottom_center, bg="gray92", height=80)
            login_but = Button(bottom_botcenter, text="LOGIN", command= lambda : self.get_log(), width=20, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")


            center_Root.pack(side=TOP, fill=BOTH, expand=1)
            top_center.pack(side=TOP, fill=BOTH, expand=1)
            image_top_center.pack(pady=20)
            center_center.pack(side=TOP, fill=BOTH, expand=1)
            sub_title.pack(pady=10)
            bottom_center.pack(side=TOP, fill=BOTH, expand=1)
            top_botcenter.pack(side=TOP, fill=BOTH, expand=1)
            left_top_bot.pack(side=LEFT, fill=BOTH, expand=1)
            name_label.pack(pady=10, fill=BOTH, expand=1)
            pass_label.pack(pady=10, fill=BOTH, expand=1)
            right_top_bot.pack(side=LEFT, fill=BOTH, expand=1)
            top_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
            bottom_right_top_bot.pack(side=TOP, fill=BOTH, expand=1)
            self.name_box.pack(side=LEFT, pady=10)
            self.pass_box.pack(side=LEFT, pady=10)
            bottom_botcenter.pack(side=TOP, fill=BOTH, expand=1)
            login_but.pack(pady=20)


            #*****************lower block*****************************
            bottom_Root = Frame(root, bg="light blue", height=50)
            copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof & Zubair Ali 2020", bg="light blue", font=('arial',12,'bold'))

            bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
            copyRight.pack(pady=10)

        def clear(self):
            self.name_box.delete(0, END)
            self.pass_box.delete(0, END)

        def get_log(self):
            if self.name_box.get() == "admin" and self.pass_box.get() == "1234":
                messagebox.showinfo("Successfull!!","Boss you are login", parent=self.root)
                self.clear()
                call_adminsys()
            else:
                messagebox.showerror("Wrong Login", "Please enter correct username & password", parent=self.root)
                self.clear()

    root = Toplevel()
    obj = get_admin(root)
    voice_loginadmin.wishme()
    mainloop()

