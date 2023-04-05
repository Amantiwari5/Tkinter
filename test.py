# Import the library tkinter
from tkinter import *
from tkinter import messagebox
from  PIL import ImageTk, Image

root=Tk()
root.title('Login')
root.geometry("1500x800")
root.config(bg="#380038")
root.resizable(False,False)



img = Image.open('login.png')
img = img.resize((900,900))
img = ImageTk.PhotoImage(img)
Label(root, image=img,bg='white').place(x=0,y=0)

#frame
frame=Frame(root,width=350,height=400,bg="white")
frame.place(x=1000,y=190)

#head
heading=Label(frame,text='Sign in',fg="#57a1f8",bg='white',font=('Mircosoft YaHei UI Light',23,'bold'))
heading.place(x=120,y=100)
img1=Image.open('R.png')
img1 = img1.resize((90,90))
my=ImageTk.PhotoImage(img1)
Label(frame,image=my,bg='white').place(x=120,y=5)



#usename
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Mircosoft YaHei UI Light',11))
user.place(x=30,y=170)
user.insert(0,'Username')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=200)
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


#password
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')
code=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Mircosoft YaHei UI Light',11))
code.place(x=30,y=220)
code.insert(0,'Password')
Frame(frame,width=295,height=2,bg='black').place(x=25,y=250)
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)


#button
Button(frame,width=39,pady=7,text='Sign In',bg='#57a1f8',fg='white',border=0).place(x=25,y=270)
lable=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Mircosoft YaHei UI Light',9))
lable.place(x=75,y=310)
sign_up=Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8')
sign_up.place(x=210,y=310)


root.mainloop()