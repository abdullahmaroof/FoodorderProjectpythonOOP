from tkinter import *
from PIL import ImageTk, Image
from LoginGUI import signin
from Final_Project.Signup_GUI import call_signup
from Final_Project.admin_login_GUI import call_adminlogin
from Final_Project.voice_system import call_voice


class main_system:
    def __init__(self, root):
        self.root = root
        root.geometry("800x470")
        root.title('Online Food Order System')
        root.iconbitmap(r'buy_online_5Wq_icon.ico')
        call_voice.wishme()
        #*****************upper block*****************************
        upper_Root = Frame(root, bg="light blue", height=100)
        title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial',28,'bold','underline'))

        upper_Root.pack(side=TOP, fill=BOTH, expand=1)
        title.pack(pady=30)

        #*****************center block*****************************
        center_Root = Frame(root, bg="gray92", height=320)
        top_center = Frame(center_Root, bg="gray92", height=140)
        self.pic = Image.open("shopping-bag.png")
        self.resized = self.pic.resize((150, 100), Image.ANTIALIAS)
        self.mypic = ImageTk.PhotoImage(self.resized)
        image_top_center = Label(top_center, image = self.mypic)
        center_center = Frame(center_Root, bg="gray92", height=80)
        left_center_cenroot = Frame(center_center, bg="gray92", height=80)
        login_but = Button(left_center_cenroot, text="LOGIN", command= lambda : signin(), width=25, height=2, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
        right_center_cenroot = Frame(center_center, bg="gray92", height=80)
        signup_but = Button(right_center_cenroot, text="SIGNUP", command= lambda : call_signup(), width=25, height=2, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
        bottom_center = Frame(center_Root, bg="gray92", height=80)
        loginadmin_but = Button(bottom_center, text="LOGIN As ADMIN", command= lambda : call_adminlogin(), width=25, height=2, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

        center_Root.pack(side=TOP, fill=BOTH, expand=1)
        top_center.pack(side=TOP, fill=BOTH, expand=1)
        image_top_center.pack(pady=20)
        center_center.pack(side=TOP, fill=BOTH, expand=1)
        left_center_cenroot.pack(side=LEFT, fill=BOTH, expand=1)
        login_but.pack(pady=20)
        right_center_cenroot.pack(side=LEFT, fill=BOTH, expand=1)
        signup_but.pack(pady=20)
        bottom_center.pack(side=TOP, fill=BOTH, expand=1)
        loginadmin_but.pack(pady=20)


        #*****************bottom block*****************************
        bottom_Root = Frame(root, bg="light blue", height=50)
        copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof & Zubair Ali 2020", bg="light blue", font=('arial',12,'bold'))

        bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
        copyRight.pack(pady=10)

root = Tk()
obj = main_system(root)
mainloop()

