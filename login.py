from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

root=Tk()
root.geometry("854x480+50+50")
root.title("user login")

root.resizable(False,False)

def submit():
    if userEntry.get()=="" or passwordentry.get()=="":
        messagebox.showerror("Error","Feilds can not be empty")

    elif userEntry.get()=="Sudip" and passwordentry.get()=="1234":
        messagebox.showinfo("success","welcome")
        root.destroy()
    
        import SMS
    
    else:
        messagebox.showerror("Error","wrong username or password")


backgroundImage=ImageTk.PhotoImage(file="projectpicwhite1.jpg")
bglabel=Label(root,image=backgroundImage)
bglabel.pack()

login=Frame(root,bg="white")
login.place(x=250,y=15)


logoimage=PhotoImage(file="mainicon.png")
logoLabel=Label(login,image=logoimage,bg="white")
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)

userimage=PhotoImage(file="username.png")
userlabel=Label(login,image=userimage,text="username",compound=LEFT,font=("times new roman", 20 ,"bold"),bg="white")
userlabel.grid(row=1,column=0,pady=10)

userEntry=Entry(login,font=("times new roman", 16 ,"bold"),bg="white",bd=5,cursor="hand2")
userEntry.grid(row=1,column=1,pady=10)


passwordimage=PhotoImage(file="password.png")
passwordLabel=Label(login,text="password",image=passwordimage,bg="white",compound=LEFT,font=("times new roman",20,"bold"))
passwordLabel.grid(row=2,column=0,pady=10)

passwordentry=Entry(login,font=("times new roman", 16 ,"bold"),bg="white",bd=5,cursor="hand2")
passwordentry.grid(row=2,column=1,pady=10)



button=Button(login,text="login",command=submit,font=("times new roman", 16 ,"bold"),bg="Slate blue1",fg="black",bd=5,padx=20,cursor="hand2")
button.grid(row=3,column=1)

root.mainloop()
