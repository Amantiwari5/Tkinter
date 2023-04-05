# Import the library tkinter
from tkinter import *
from tkinter import ttk
import os
from  PIL import ImageTk, Image

def Reg():
    try:
        main.winfo_exists()
        main.destroy()
        Reg1()
        # pass
    except: 
        root.winfo_exists()
        root.destroy()
        Reg1()
def Reg1():
    global reg
    reg=Tk()
    reg.title("Fuck management system")
    reg.geometry("1500x1500")
    reg.configure(bg="white")
    reg.resizable(False,False)
    
    #image
    img1 = Image.open('logo.png')
    img1 = img1.resize((550,400))
    img1 = ImageTk.PhotoImage(img1)
    Label(reg, image=img1,bg='white').place(x=0,y=-100,relwidth=1)
    l1 = Label(reg, text="---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg="white",font=("bold"))
    l1.place(x=0,y=110,relwidth=1)
    
    #buttons and entries
    
    
    
    
    
    # Creating Menubar
    menubar = Menu(reg)

    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Menu', menu = file)
    file.add_command(label ='Log In', command = login)
    file.add_separator()
    file.add_command(label ='Exit', command = reg.destroy)

    # Adding Edit Menu and commands
    # edit = Menu(root, tearoff = 0)
    # menubar.add_cascade(label ='Edit', menu = edit)
    # edit.add_command(label ='Cut', command = None)
    # edit.add_command(label ='Copy', command = None)
    # edit.add_command(label ='Paste', command = None)
    # edit.add_command(label ='Select All', command = None)
    # edit.add_separator()
    # edit.add_command(label ='Find...', command = None)
    # edit.add_command(label ='Find again', command = None)

    # Adding Help Menu
    help_ = Menu(reg, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='About Dev.', command = None)
    help_.add_separator()
    help_.add_command(label ='About Bank', command = None)

    # display Menu
    reg.config(menu = menubar)
    
    reg.mainloop()
def login():
    try:
        main.winfo_exists()
        main.destroy()
        log()
    except:
        reg.winfo_exists()
        reg.destroy()
        log()
def log():
    global root
    root=Tk()
    root.title('Login')
    root.geometry("1500x800")
    root.config(bg="#b0c4de")
    root.resizable(False,False)


    #image
    img = Image.open('login.png')
    img = img.resize((900,900))
    img = ImageTk.PhotoImage(img)
    Label(root, image=img,bg='white').place(x=0,y=0)


    #frame
    frame=Frame(root,width=450,height=600,bg="white")
    frame.place(x=985,y=105)


    #head
    heading=Label(frame,text='Sign in',fg="#57a1f8",bg='white',font=('Mircosoft YaHei UI Light',30,'bold'))
    heading.place(x=155,y=120)
    img1=Image.open('R.png')
    img1 = img1.resize((90,90))
    my=ImageTk.PhotoImage(img1)
    Label(frame,image=my,bg='white').place(x=180,y=20)


    #usename
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='gray',border=0,bg="white",font=('Mircosoft YaHei UI Light',20))
    user.place(x=95,y=240)
    user.insert(0,'Username')
    Frame(frame,width=295,height=2,bg='black',relief='solid').place(x=100,y=280)
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)


    #password
    def on_enter(e):
        code.delete(0,'end')
    def on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    code=Entry(frame,width=25,fg='gray',border=0,bg="white",font=('Mircosoft YaHei UI Light',20))
    code.place(x=95,y=310)
    code.insert(0,'Password')
    Frame(frame,width=295,height=2,bg='black').place(x=100,y=350)
    code.bind('<FocusIn>',on_enter)
    code.bind('<FocusOut>',on_leave)


    #button
    Button(frame,width=25,text='Sign In',bg='#57a1f8',fg='white',border=0,font=('Mircosoft YaHei UI Light',15)).place(x=100,y=420)
    lable=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Mircosoft YaHei UI Light',12))
    lable.place(x=100,y=480)
    sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',command=Reg,cursor='hand2',fg='#57a1f8',font=('Mircosoft YaHei UI Light',12))
    sign_up.place(x=270,y=480)

    # Creating Menubar
    menubar = Menu(root)

    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Menu', menu = file)
    file.add_command(label ='Registraction', command = Reg)
    file.add_separator()
    file.add_command(label ='Exit', command = root.destroy)

    # Adding Edit Menu and commands
    # edit = Menu(root, tearoff = 0)
    # menubar.add_cascade(label ='Edit', menu = edit)
    # edit.add_command(label ='Cut', command = None)
    # edit.add_command(label ='Copy', command = None)
    # edit.add_command(label ='Paste', command = None)
    # edit.add_command(label ='Select All', command = None)
    # edit.add_separator()
    # edit.add_command(label ='Find...', command = None)
    # edit.add_command(label ='Find again', command = None)

    # Adding Help Menu
    help_ = Menu(root, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='About Dev.', command = None)
    help_.add_separator()
    help_.add_command(label ='About Bank', command = None)

    # display Menu
    root.config(menu = menubar)

    root.mainloop()



def first():
    #Main
    global main
    main=Tk()
    main.title("Fuck management system")
    main.geometry("1500x900")
    main.configure(bg="white")
    main.resizable(False,False)

    #Image import
    img = Image.open('fst.png')
    img = img.resize((900,900))
    img = ImageTk.PhotoImage(img)
    Label(main, image=img,bg='white').place(x=0,y=80)

    img1 = Image.open('logo.png')
    img1 = img1.resize((550,400))
    img1 = ImageTk.PhotoImage(img1)
    Label(main, image=img1,bg='white').place(x=910,y=250)

    # Label
    Label(main, text = " India's Most Secure Bank ", font=('Calibri',16,"bold"),bg="white").place(x=1080,y=480)

    #Buttons
    Button(main, text="Register", font=('Calibri',12),width=40,height=2,command=Reg,bg='white',border=1,activebackground="light blue",relief="groove").place(x=1030,y=600)
    Button(main, text="Log In", font=('Calibri',12),width=40,height=2,command=login,bg='white',border=1,activebackground="light blue",relief="groove").place(x=1030,y=680)


    # Creating Menubar
    menubar = Menu(main)

    # Adding File Menu and commands
    file = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Menu', menu = file)
    file.add_command(label ='Regsistraction', command = Reg)
    file.add_command(label ='Log In', command = login)
    file.add_separator()
    file.add_command(label ='Exit', command = main.destroy)

    # Adding Edit Menu and commands
    # edit = Menu(main, tearoff = 0)
    # menubar.add_cascade(label ='Edit', menu = edit)
    # edit.add_command(label ='Cut', command = None)
    # edit.add_command(label ='Copy', command = None)
    # edit.add_command(label ='Paste', command = None)
    # edit.add_command(label ='Select All', command = None)
    # edit.add_separator()
    # edit.add_command(label ='Find...', command = None)
    # edit.add_command(label ='Find again', command = None)

    # Adding Help Menu
    help_ = Menu(main, tearoff = 0)
    menubar.add_cascade(label ='Help', menu = help_)
    help_.add_command(label ='Tk Help', command = None)
    help_.add_command(label ='About Dev.', command = None)
    help_.add_separator()
    help_.add_command(label ='About Bank', command = None)

    # display Menu
    main.config(menu = menubar)

    main.mainloop()
first()