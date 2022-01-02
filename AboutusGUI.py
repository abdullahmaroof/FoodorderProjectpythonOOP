from tkinter import *
from PIL import ImageTk, Image
from VoiceSystem import voice_aboutus, voice_aboutabdullah, voice_aboutZUBAIR

def call_aboutus():
    root = Toplevel()


    root.geometry("800x730")
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
    sub_title = Label(center_center, text="About Us", bg="gray92", font=('arial',20,'underline','bold'))
    bottom_center = Frame(center_Root, bg="gray92", height=250)
    left_bcenter = Frame(bottom_center, bg="gray92", height=350)
    right_bcenter = Frame(bottom_center, bg="gray92", height=350)
    ab_pic = Image.open("abdullah.png")
    ab_image = ImageTk.PhotoImage(ab_pic)
    ab_pic_label = Label(left_bcenter, image=ab_image, bg="gray92")
    ab_info_but = Button(left_bcenter, text="Abdullah Maroof", command = lambda : voice_aboutabdullah.wishme(), width=25, height=2, bg="light blue",font=('arial', 10, 'bold'), activebackground="black", activeforeground="white")
    zb_pic = Image.open("zubair.png")
    zb_image = ImageTk.PhotoImage(zb_pic)
    zb_pic_label = Label(right_bcenter, image=zb_image, bg="gray92")
    zb_info_but = Button(right_bcenter, text="Zubair Ali", command= lambda : voice_aboutZUBAIR.wishme(), width=25, height=2, bg="light blue", font=('arial', 10, 'bold'), activebackground="black", activeforeground="white")




    center_Root.pack(side=TOP, fill=BOTH, expand=1)
    top_center.pack(side=TOP, fill=BOTH, expand=1)
    image_top_center.pack(pady=20)
    center_center.pack(side=TOP, fill=BOTH, expand=1)
    sub_title.pack(pady=10)
    bottom_center.pack(side=TOP, fill=BOTH, expand=1, padx=40, pady=10)
    left_bcenter.pack(side=LEFT, fill=BOTH, expand=1)
    right_bcenter.pack(side=LEFT, fill=BOTH, expand=1)
    ab_pic_label.pack(side=TOP)
    ab_info_but.pack(side=BOTTOM, pady=5)
    zb_pic_label.pack(side=TOP)
    zb_info_but.pack(side=BOTTOM, pady=5)

    #*****************bottom block*****************************
    bottom_Root = Frame(root, bg="light blue", height=50)
    copyRight = Label(bottom_Root, text=" © Copy Rights Reserved, Abdullah Maroof & Zubair Ali 2020", bg="light blue", font=('arial',12,'bold'))

    bottom_Root.pack(side=BOTTOM, fill=BOTH, expand=1)
    copyRight.pack(pady=10)
    voice_aboutus.wishme()
    mainloop()

