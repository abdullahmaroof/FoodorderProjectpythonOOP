from tkinter import *
from PIL import ImageTk, Image
from Final_Project.voice_system import voice_admin
from Final_Project.Menu_Report import excelMENUReportGeneration
from Final_Project.User_Report import excelUSERReportGeneration
from Final_Project.Bill_report import excelbillReportGeneration
#from Final_Project.excel_oracle import exceloracleReportGeneration


def call_adminsys():
    class get_admin():
        def __init__(self, root):
            self.root = root
            root.geometry("800x550")
            root.title('Online Food Order System')
            root.iconbitmap(r'buy_online_5Wq_icon.ico')
            #*****************upper block*****************************
            upper_Root = Frame(root, bg="light blue", height=100)
            title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial', 28, 'bold', 'underline'))

            upper_Root.pack(side=TOP, fill=BOTH, expand=1)
            title.pack(pady=30)

            #*****************center block*****************************
            center_Root = Frame(root, bg="gray92", height=200)
            top_center = Frame(center_Root, bg="gray92", height=140)
            self.pic = Image.open("shopping-bag.png")
            self.resized = self.pic.resize((150, 100), Image.ANTIALIAS)
            self.mypic = ImageTk.PhotoImage(self.resized)
            image_top_center = Label(top_center, image = self.mypic)
            center_center = Frame(center_Root, bg="gray92", height=80)
            sub_title = Label(center_center, text="Welcome To System", bg="gray92", font=('arial',20,'underline','bold'))
            bottom_center = Frame(center_Root, bg="gray92", height=80)
            left_bottom_cenroot = Frame(bottom_center, bg="", height=80)
            info_but = Button(left_bottom_cenroot, text="Users Data", command= lambda : excelUSERReportGeneration(), width=25, height=2, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            right_bottom_cenroot = Frame(bottom_center, bg="gray92", height=80)
            aboutus_but = Button(right_bottom_cenroot, text="Bills Data", command= lambda : excelbillReportGeneration(), width=25, height=2, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
            last_center = Frame(center_Root, bg="gray92", height=80)
            left_last_cenroot = Frame(last_center, bg="gray92", height=80)
            menu_but = Button(left_last_cenroot, text="Menu Data", command=lambda: excelMENUReportGeneration(),
                              width=25, height=2, bg="light blue", font=('arial', 10, 'bold'), activebackground="black",
                              activeforeground="white")
            right_last_cenroot = Frame(last_center, bg="gray92", height=80)
            join_but = Button(right_last_cenroot, text="Menu & Bills Data", command=lambda: exceloracleReportGeneration(),
                                 width=25, height=2, bg="light blue", font=('arial', 10, 'bold'),
                                 activebackground="black", activeforeground="white")

            center_Root.pack(side=TOP, fill=BOTH, expand=1)
            top_center.pack(side=TOP, fill=BOTH, expand=1)
            image_top_center.pack(pady=20)
            center_center.pack(side=TOP, fill=BOTH, expand=1)
            sub_title.pack(pady=10)
            bottom_center.pack(side=TOP, fill=BOTH, expand=1)
            left_bottom_cenroot.pack(side=LEFT, fill=BOTH, expand=1)
            info_but.pack(pady=20)
            right_bottom_cenroot.pack(side=LEFT, fill=BOTH, expand=1)
            aboutus_but.pack(pady=20)
            last_center.pack(side=TOP, fill=BOTH, expand=1)
            left_last_cenroot.pack(side=LEFT, fill=BOTH, expand=1)
            menu_but.pack(pady=20)
            right_last_cenroot.pack(side=LEFT, fill=BOTH, expand=1)
            join_but.pack(pady=20)


            #*****************bottom block*****************************
            bottom_Root = Frame(root, bg="light blue", height=50)
            copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof & Zubair Ali 2020", bg="light blue", font=('arial',12,'bold'))

            bottom_Root.pack(side=TOP, fill=BOTH, expand=1)
            copyRight.pack(pady=10)

    root = Toplevel()
    obj = get_admin(root)
    voice_admin.wishme()
    mainloop()