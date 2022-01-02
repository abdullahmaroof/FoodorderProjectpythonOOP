from tkinter import *
from PIL import ImageTk, Image
from Final_Project.foodmenu_GUI import call_menu
from VoiceSystem import voice_system
from Final_Project.aboutus_gui import call_aboutus


def call_system():
    root = Toplevel()
    root.geometry("800x450")
    root.title('Online Food Order System')
    root.iconbitmap(r'buy_online_5Wq_icon.ico')
    #*****************upper block*****************************
    upper_Root = Frame(root, bg="light blue", height=100)
    title = Label(upper_Root, text="Online Food Order System", bg="light blue", font=('arial', 28, 'bold', 'underline'))

    upper_Root.pack(side=TOP, fill=BOTH, expand=1)
    title.pack(pady=30)

    #*****************center block*****************************
    center_Root = Frame(root, bg="gray92", height=400)
    top_center = Frame(center_Root, bg="gray92", height=140)
    pic = Image.open("shopping-bag.png")
    resized = pic.resize((150, 100), Image.ANTIALIAS)
    mypic = ImageTk.PhotoImage(resized)
    image_top_center = Label(top_center, image = mypic)
    center_center = Frame(center_Root, bg="gray92", height=80)
    sub_title = Label(center_center, text="Welcome To System", bg="gray92", font=('arial',20,'underline','bold'))
    bottom_center = Frame(center_Root, bg="gray92", height=80)
    left_bottom_cenroot = Frame(bottom_center, bg="", height=80)
    info_but = Button(left_bottom_cenroot, text="Order Food", command= lambda : call_menu(), width=25, height=2, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")
    right_bottom_cenroot = Frame(bottom_center, bg="gray92", height=80)
    aboutus_but = Button(right_bottom_cenroot, text="About us", command= lambda : call_aboutus(), width=25, height=2, bg="light blue", font=('arial',10,'bold'), activebackground="black", activeforeground="white")

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

    #*****************bottom block*****************************
    bottom_Root = Frame(root, bg="light blue", height=50)
    copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof & Zubair Ali 2020", bg="light blue", font=('arial',12,'bold'))

    bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
    copyRight.pack(pady=10)
    voice_system.wishme()
    mainloop()
