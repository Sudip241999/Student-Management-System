from tkinter import *
import time
from tkinter import ttk
import pymysql
from tkinter import messagebox
from tkinter import filedialog
import pandas as ps

root1=Tk()


# funtions are here :

# function to search student :
def Exit():
    value=messagebox.askyesno("Confirm","do you want to exit?")
    if value:
        root1.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfile(defaultextension=".csv")
    index=studentTable.get_children()
    l=[]
    for i in index:
        content=studentTable.item(i)
        data_list=content["values"]
        l.append(data_list)
    table=ps.DataFrame(l,columns=["id","name","mobile","email","address","gender","DOB","date","time"])
    table.to_csv(url,index=False)
    messagebox.showinfo("Success","Exported")


    


def update_student():

    def update_data():
        query="update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s"
        currentdate=time.strftime("%d/%m/%Y")
        currenttime=time.strftime("%H:%M:%S")
        mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),DOBEntry.get(),currentdate,currenttime,idEntry.get()))
        con.commit()
        messagebox.showinfo("info",f"this id {idEntry.get()} is updated successfully!")
        updatewindow.destroy()
        query="select * from student"
        mycursor.execute(query)

        studentTable.delete(*studentTable.get_children())
        fetched_data=mycursor.fetchall()
        for i in fetched_data:
            studentTable.insert("",END,values=i)
    
    updatewindow=Toplevel(background="Antique white1")
    updatewindow.resizable(False,False)
    updatewindow.grab_set()
    idLabel=Label(updatewindow,text="ID",font=("arial",15,"bold"),bg="Antique white1")
    idLabel.grid(row=0,column=0,padx=30,pady=15)

    idEntry=Entry(updatewindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    NameLabel=Label(updatewindow,text="NAME",font=("arial",15,"bold"),bg="Antique white1")
    NameLabel.grid(row=1,column=0,padx=30,pady=15)

    nameEntry=Entry(updatewindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    phoneLabel=Label(updatewindow,text="PHONE",font=("arial",15,"bold"),bg="Antique white1")
    phoneLabel.grid(row=2,column=0,padx=30,pady=15)

    phoneEntry=Entry(updatewindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(updatewindow,text="EMAIL",font=("arial",15,"bold"),bg="Antique white1")
    emailLabel.grid(row=3,column=0,padx=30,pady=15)

    emailEntry=Entry(updatewindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)


    addressLabel=Label(updatewindow,text="ADDRESS",font=("arial",15,"bold"),bg="Antique white1")
    addressLabel.grid(row=4,column=0,padx=30,pady=15)

    addressEntry=Entry(updatewindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel=Label(updatewindow,text="GENDER",font=("arial",15,"bold"),bg="Antique white1")
    genderLabel.grid(row=5,column=0,padx=30,pady=15)

    genderEntry=Entry(updatewindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    DOBLabel=Label(updatewindow,text="D.O.B",font=("arial",15,"bold"),bg="Antique white1")
    DOBLabel.grid(row=6,column=0,padx=30,pady=15)

    DOBEntry=Entry(updatewindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    DOBEntry.grid(row=6,column=1,pady=15,padx=10)


    update=Button(updatewindow,text="Update",font=("roman",12,"bold"),padx=25,pady=15,command=update_data)
    update.grid(row=7,column=1,padx=15,pady=15)


    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    list_data=content["values"]
    idEntry.insert(0,list_data[0])
    nameEntry.insert(0,list_data[1])
    phoneEntry.insert(0,list_data[2])
    emailEntry.insert(0,list_data[3])
    addressEntry.insert(0,list_data[4])
    genderEntry.insert(0,list_data[5])
    DOBEntry.insert(0,list_data[6])

    

    

def show_data():
    query="select * from student"
    mycursor.execute(query)
    studentTable.delete(*studentTable.get_children())
    fetchedData=mycursor.fetchall()
    for i in fetchedData:
        studentTable.insert("",END,values=i)


def delete_student():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    contentID=content['values'][0]
    query="delete from student where id=%s"
    mycursor.execute(query,contentID)
    con.commit()
    messagebox.showinfo("Info",f"this id {contentID} is deleted successfully!")

    query="select * from student"
    mycursor.execute(query)

    fetchedData=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for i in fetchedData:
        studentTable.insert("",END,values=i)


def search_student():

    def search_data():
        query="select * from student where id=%s or name=%s or address=%s or email=%s or mobile=%s or gender=%s or dob=%s"
        mycursor.execute(query,(idEntry.get(),nameEntry.get(),addressEntry.get(),emailEntry.get(),phoneEntry.get(),genderEntry.get(),DOBEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetcheddata=mycursor.fetchall()
        for i in fetcheddata:

            studentTable.insert("",END,values=i)


    searchWindow=Toplevel(background="Antique white1")
    searchWindow.resizable(False,False)
    searchWindow.grab_set()
    idLabel=Label(searchWindow,text="ID",font=("arial",15,"bold"),bg="Antique white1")
    idLabel.grid(row=0,column=0,padx=30,pady=15)

    idEntry=Entry(searchWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    NameLabel=Label(searchWindow,text="NAME",font=("arial",15,"bold"),bg="Antique white1")
    NameLabel.grid(row=1,column=0,padx=30,pady=15)

    nameEntry=Entry(searchWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    phoneLabel=Label(searchWindow,text="PHONE",font=("arial",15,"bold"),bg="Antique white1")
    phoneLabel.grid(row=2,column=0,padx=30,pady=15)

    phoneEntry=Entry(searchWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(searchWindow,text="EMAIL",font=("arial",15,"bold"),bg="Antique white1")
    emailLabel.grid(row=3,column=0,padx=30,pady=15)

    emailEntry=Entry(searchWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)


    addressLabel=Label(searchWindow,text="ADDRESS",font=("arial",15,"bold"),bg="Antique white1")
    addressLabel.grid(row=4,column=0,padx=30,pady=15)

    addressEntry=Entry(searchWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel=Label(searchWindow,text="GENDER",font=("arial",15,"bold"),bg="Antique white1")
    genderLabel.grid(row=5,column=0,padx=30,pady=15)

    genderEntry=Entry(searchWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    DOBLabel=Label(searchWindow,text="D.O.B",font=("arial",15,"bold"),bg="Antique white1")
    DOBLabel.grid(row=6,column=0,padx=30,pady=15)

    DOBEntry=Entry(searchWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    DOBEntry.grid(row=6,column=1,pady=15,padx=10)


    search=Button(searchWindow,text="Search",font=("roman",12,"bold"),padx=25,pady=15,command=search_data)
    search.grid(row=7,column=1,padx=15,pady=15)

#function to add student : 
def add_student():


    def add_data():
        if idEntry.get()=="" or nameEntry.get()=="" or phoneEntry.get()=="" or emailEntry.get()=="" or addressEntry.get()=="" or genderEntry.get()=="" or DOBEntry.get()=="":
            messagebox.showerror("Error","All fields are required",parent=addWindow)
        else:
            currdate=time.strftime("%d/%m/%Y")
            currtime=time.strftime("%H:%M:%S")
            try:
                query="insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),DOBEntry.get(),currdate,currtime))
                con.commit()
                result=messagebox.askyesno("Info","Data added successfully .Do you want to clean the form?",parent=addWindow)
                if result==True:
                    idEntry.delete(0,END)
                    nameEntry.delete(0,END)
                    phoneEntry.delete(0,END)
                    emailEntry.delete(0,END)
                    addressEntry.delete(0,END)
                    genderEntry.delete(0,END)
                    DOBEntry.delete(0,END)

                else:
                    pass
            except:
                messagebox.showerror("Error","Id can not be repeated!",parent=addWindow)
                return
            

            query="select * from student"
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for i in fetched_data:
                studentTable.insert("",END,values=i)
                



    #creating a new gui on a top of a gui so we are using toplevel class :


    addWindow=Toplevel(background="Antique white1")
    addWindow.resizable(False,False)
    addWindow.grab_set()
    idLabel=Label(addWindow,text="ID",font=("arial",15,"bold"),bg="Antique white1")
    idLabel.grid(row=0,column=0,padx=30,pady=15)

    idEntry=Entry(addWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    NameLabel=Label(addWindow,text="NAME",font=("arial",15,"bold"),bg="Antique white1")
    NameLabel.grid(row=1,column=0,padx=30,pady=15)

    nameEntry=Entry(addWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)

    phoneLabel=Label(addWindow,text="PHONE",font=("arial",15,"bold"),bg="Antique white1")
    phoneLabel.grid(row=2,column=0,padx=30,pady=15)

    phoneEntry=Entry(addWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)

    emailLabel=Label(addWindow,text="EMAIL",font=("arial",15,"bold"),bg="Antique white1")
    emailLabel.grid(row=3,column=0,padx=30,pady=15)

    emailEntry=Entry(addWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)


    addressLabel=Label(addWindow,text="ADDRESS",font=("arial",15,"bold"),bg="Antique white1")
    addressLabel.grid(row=4,column=0,padx=30,pady=15)

    addressEntry=Entry(addWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)

    genderLabel=Label(addWindow,text="GENDER",font=("arial",15,"bold"),bg="Antique white1")
    genderLabel.grid(row=5,column=0,padx=30,pady=15)

    genderEntry=Entry(addWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    genderEntry.grid(row=5,column=1,pady=15,padx=10)

    DOBLabel=Label(addWindow,text="D.O.B",font=("arial",15,"bold"),bg="Antique white1")
    DOBLabel.grid(row=6,column=0,padx=30,pady=15)

    DOBEntry=Entry(addWindow,font=("roman",12,"bold"),bd=2,relief="sunken",width=20)
    DOBEntry.grid(row=6,column=1,pady=15,padx=10)


    submit=Button(addWindow,text="Submit",font=("roman",12,"bold"),padx=25,pady=15,command=add_data)
    submit.grid(row=7,column=1,padx=15,pady=15)


def connect_database():

    def connectWithData():
        global mycursor
        global con
        try:
            con=pymysql.connect(host=hostEntry.get(),user=userEntry.get(),password=passwordEntry.get())
            mycursor=con.cursor()
            messagebox.showinfo("SUCCESS","Database connection is successful!",parent=topwindow)
            topwindow.destroy()
        #enable all buttons : 
            addstudent.config(state=NORMAL)
            updatestudent.config(state=NORMAL)
            exportstudent.config(state=NORMAL)
            showstudent.config(state=NORMAL)
            Exit.config(state=NORMAL)
            searchstudent.config(state=NORMAL)
            deletestudent.config(state=NORMAL)
        except:
            messagebox.showerror("Error","Invalid details!",parent=topwindow)
        try:

            query="create database StudentManagementSystem"
            mycursor.execute(query)
            query="use StudentManagementSystem"
            mycursor.execute(query)

            query="create table student(id int not null primary key,Name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))"
            mycursor.execute(query)
        except:
            query="use StudentManagementSystem"
            mycursor.execute(query)
        


        


    topwindow=Toplevel(background="Antique white1")
    topwindow.grab_set()
    topwindow.geometry("470x250+730+230")
    topwindow.title("Database connection")
    topwindow.resizable(0,0)


    # create Host name Label :

    hostLabel=Label(topwindow,text="Host Name",font=("arial",15,"bold"),bg="Antique white1")
    hostLabel.grid(row=0,column=0,padx=20)


    hostEntry=Entry(topwindow,font=("roman",12,"bold"),relief="sunken",bd=2)
    hostEntry.grid(row=0,column=1,pady=10)


    userName=Label(topwindow,text="User Name",font=("arial",15,"bold"),bg="Antique white1")
    userName.grid(row=1,column=0)

    userEntry=Entry(topwindow,font=("roman",12,"bold"),relief="sunken",bd=2)
    userEntry.grid(row=1,column=1)

    passwordLabel=Label(topwindow,text="Password",font=("arial",15,"bold"),bg="Antique white1")
    passwordLabel.grid(row=2,column=0,pady=10)

    passwordEntry=Entry(topwindow,font=("roman",12,"bold"),bd=2,relief="sunken")
    passwordEntry.grid(row=2,column=1,pady=10)


    # creating a button to connect:

    conectButton=Button(topwindow,text="connect",font=("arial",12,"bold"),padx=10,bg="Slate blue3",command=connectWithData)
    conectButton.grid(row=3,column=1)


def clock():
    date=time.strftime("%d/%m/%Y")
    CURRENTtime=time.strftime("%H:%M:%S")
    dateLabel.config(text=f"   Date : {date}\n Time : {CURRENTtime}")
    dateLabel.after(1000,clock)


count=0
test=''
def slider():
    global test
    global count
    if count==len(s):
        count=0
        test=""
    test=test+s[count]
    count+=1
    sliderLabel.config(text=test) 
    sliderLabel.after(300,slider)   




# GUI is here :



root1.geometry("1174x680+50+20")

root1.resizable(False,False)
root1.title("Student Management System")

# Date time Label :

dateLabel=Label(root1,font=("times new roman",18,"bold"),fg="Violet red1")
dateLabel.place(x=5,y=5)
clock()

# Slider is here :
s="Student Management System"
sliderLabel=Label(root1,text=s,font=("times new roman",28,"italic bold"),width=30,fg="Slate blue4")
sliderLabel.place(x=250,y=0)
slider()

# creating a button connect to database :

connect=Button(root1,text="Connect to Database",font=("times new roman",12,"bold"),relief="raised",padx=10,bg="orange red",command=connect_database)
connect.place(x=1000,y=0)


# creating left frame :

leftFrame=Frame(root1)
leftFrame.place(x=50,y=80,width=300,height=600)


# adding logo :

logoimage=PhotoImage(file="iconClass.png")
logoLabel=Label(leftFrame,image=logoimage)
logoLabel.grid(row=0,column=0)

# creating buttons like add student,delete,export etc...... :

addstudent=Button(leftFrame,text="Add Student",padx=20,font=("times new roman",14,"bold"),relief="raised",width=15,bg="Slate blue1",state=DISABLED,command=add_student)
addstudent.grid(row=2,column=0,pady=15)


deletestudent=Button(leftFrame,text="Delete Student",padx=20,font=("times new roman",14,"bold"),width=15,bg="Slate blue1",state=DISABLED,command=delete_student)
deletestudent.grid(row=3,column=0,pady=20)


searchstudent=Button(leftFrame,text="Search Student",padx=20,font=("times new roman",14,"bold"),width=15,bg="Slate blue1",state=DISABLED,command=search_student)
searchstudent.grid(row=4,column=0,pady=20)


exportstudent=Button(leftFrame,text="export data",padx=20,font=("times new roman",14,"bold"),width=15,bg="Slate blue1",state=DISABLED,command=export_data)
exportstudent.grid(row=5,column=0,pady=20)


updatestudent=Button(leftFrame,text="Update Student",padx=20,font=("times new roman",14,"bold"),width=15,bg="Slate blue1",state=DISABLED,command=update_student)
updatestudent.grid(row=6,column=0,pady=20)

showstudent=Button(leftFrame,text="Show Student",padx=20,font=("times new roman",14,"bold"),width=15,bg="Slate blue1",state=DISABLED,command=show_data)
showstudent.grid(row=7,column=0,pady=20)


Exit=Button(leftFrame,text="Exit",padx=20,font=("times new roman",14,"bold"),bg="Slate blue1",width=15,state=DISABLED,command=Exit)
Exit.grid(row=8,column=0,pady=18)



# creating right Frame :

rightFrame=Frame(root1)
rightFrame.place(x=350,y=80,width=820,height=580)

# creating scrollbar :

scrolbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrolbarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=("Id","Name","Mobile no","email","address","D.O.B","Added Date","Added time"),xscrollcommand=scrolbarX.set,yscrollcommand=scrolbarY.set)


scrolbarY.config(command=studentTable.yview)
scrolbarX.config(command=studentTable.xview)

scrolbarX.pack(side=BOTTOM,fill=X)
scrolbarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading("Id",text="ID")
studentTable.heading("Name",text="NAME")
studentTable.heading("Mobile no",text="MOBILE NO")
studentTable.heading("email",text="EMAIL")
studentTable.heading("address",text="ADDRESS")
studentTable.heading("D.O.B",text="D.O.B")
studentTable.heading("Added Date",text="ADDED DATE")
studentTable.heading("Added time",text="ADDED TIME")

studentTable.column("Id",width=50,anchor=CENTER)
studentTable.column("Name",width=200,anchor=CENTER)
studentTable.column("Mobile no",width=250,anchor=CENTER)
studentTable.column("email",width=300,anchor=CENTER)
studentTable.column("address",width=300,anchor=CENTER)
studentTable.column("D.O.B",width=100,anchor=CENTER)
studentTable.column("Added Date",width=150,anchor=CENTER)
studentTable.column("Added time",width=150,anchor=CENTER)





studentTable.config(show="headings")




root1.mainloop()