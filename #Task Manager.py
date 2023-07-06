#Task Manager
#Mysql Connection
import mysql.connector
mycon = mysql.connector.connect(host="localhost",username="root",passwd="abc123",database="tkinter_projects")
c = mycon.cursor()

from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("TASK MANAGER")
root.geometry("1920x1024")

Labe = Label(root,text = "MY TASK MANAGER",font = ("Arial",20))
Labe.pack()
'''Labe2 = Label(root,text='6-9: Inorganic Chem')
Labe2.pack(anchor='w')
Labe3 = Label(root,text='930-1230 : Organic / Physical Chemistry')
Labe3.pack(anchor='w')
Labe4 = Label(root,text='1330-1700 : Test or Physics')
Labe4.pack(anchor='w')
Labe5 = Label(root,text='1730-2100 : Maths')
Labe5.pack(anchor='w')
Labe6 = Label(root,text='2200-0030 : BITSAT PREP ***')
Labe6.pack(anchor='w')'''

#Register
def reg():
    top = Toplevel(root)
    Lab = Label(top,text="LOGIN")
    Lab.grid(row=0,column=0)
    Lab1 = Label(top,text="Username: ")
    Lab1.grid(row=1,column=0)
    e1 = Entry(top,width = 30)
    e1.grid(row=1,column=1)
    Lab2 = Label(top,text="Password: ")
    Lab2.grid(row=2,column=0)
    e2 = Entry(top,width=30)
    e2.grid(row=2,column=1)
    def save():
        an = messagebox.askquestion("Are you sure?","Do you want to create this accnt?")
        if an=='yes':
            q1 = "insert into login values('{}','{}')".format(e1.get(),e2.get())
            c.execute(q1)
            mycon.commit()
            q2 = "create table {} (todo varchar(100),doing varchar(100), done varchar(100))".format(e1.get())
            c.execute(q2)
            mycon.commit()
            but12.configure(state=DISABLED)
    but12 = Button(top,text="Save",command=save)
    but12.grid(row=3,column=0)

but11 = Button(root,text="Reg",command=reg)
but11.pack()

#Login
def stlogin():
    global e1
    global e2
    global var
    global can1
    can1 = Canvas(root)
    can1.pack()
    Lab = Label(can1,text="LOGIN")
    Lab.grid(row=0,column=0)
    Lab1 = Label(can1,text="Username: ")
    Lab1.grid(row=1,column=0)
    e1 = Entry(can1,width = 30)
    e1.grid(row=1,column=1)
    Lab2 = Label(can1,text="Password: ")
    Lab2.grid(row=2,column=0)
    e2 = Entry(can1,width=30)
    e2.grid(row=2,column=1)
    var = StringVar()
    var.set("0")
    a1 = Checkbutton(can1,text="Remember Login details",variable=var)
    a1.grid(row=3,column=1)
    q1 = "select * from remember"
    c.execute(q1)
    dat1 = c.fetchall()
    print(dat1[0][0])
    print(e1.get())
    e1.insert(0,dat1[0][0])
    e2.insert(0,dat1[0][1])
stlogin()

def login():
    q1 = "select * from login"
    c.execute(q1)
    dat3 = c.fetchall()
    user = e1.get()
    if (e1.get(),e2.get()) in dat3:
        print(var.get())
        if var.get()=='1':
            q2 = "delete from remember where LENGTH(password) > 0"
            q3 = "insert into remember values('{}','{}')".format(e1.get(),e2.get())
            c.execute(q2)
            c.execute(q3)
            mycon.commit()
        but11.destroy()
        can1.destroy()
        can = Canvas(root)
        can.pack()
        # To Do Coloumn
        lab = Label(can,text='To Do List',font=("Arial",15))
        lab.grid(row=0,column=0,sticky='n')
        task = StringVar()        #Variable creation for Radiobuttons
        task.set('')
        #q1 = "select * from to_do"
        q1 = "select todo from {}".format(user)
        c.execute(q1)
        dat = c.fetchall()
        mycon.commit()
        #creating lists for storing data
        lis=[]
        lis1 = []
        lis2=[]
        #Recovering Data from To_Do table
        a1 = []
        for i in range(len(dat)):
            if dat[i][0] != None:
                a1.append(dat[i])
        for i in range(len(a1)):
                r3 = Radiobutton(can,text=a1[i][0],variable=task,value=a1[i][0],font=("Arial",12))
                lis.append((r3,a1[i][0]))
                r3.grid(row=i+2,column=0,sticky='w')

        #Rearrangement
        def rearrange():
            #q1 = 'select * from to_do'
            q1 = 'select todo from {}'.format(user)
            c.execute(q1)
            dat=c.fetchall()
            #q2 = 'select * from doing'
            q2 = 'select doing from {}'.format(user)
            c.execute(q2)
            dat1=c.fetchall()
            #q3 = 'select * from done'
            q3 = 'select done from {}'.format(user)
            c.execute(q3)
            dat2=c.fetchall()
            #Destroying all the radiobuttons to show in ordered manner
            for l in range(len(lis)):
                lis[l][0].destroy()
            for a in range(len(lis1)):
                lis1[a][0].destroy()
            for n in range(len(lis2)):
                lis2[n][0].destroy()
            #Clearing all lists to append new / updated data in each list
            lis.clear()
            lis1.clear()
            lis2.clear()
            
            ## (Small change here that if condition added (can be removed later on))
            no1 = []
            no2 = []
            no3 = []
            for i in range(len(dat)):
                if dat[i][0]!=None:
                    no1.append(dat[i])
            for j in range(len(dat1)):
                if dat1[j][0]!=None:
                    no2.append(dat1[j])
            for k in range(len(dat2)):
                if dat2[k][0]!=None:
                    no3.append(dat2[k])

            #Recovering and updating all the data from all the tables (dat : no1 , dat1 : no2 , dat2 : no3)
            for i in range(len(no1)):
                    r8 = Radiobutton(can,text=no1[i][0],variable=task,value=no1[i][0],font=("Arial",12))
                    r8.grid(row=i+2,column=0,sticky='w')
                    lis.append((r8,no1[i][0]))
            for j in range(len(no2)):
                    r9 = Radiobutton(can,text=no2[j][0],variable=task,value=no2[j][0],font=("Arial",12))
                    r9.grid(row=j+1,column=2,sticky='w')
                    lis1.append((r9,no2[j][0]))
            for k in range(len(no3)):
                    r10 = Radiobutton(can,text=no3[k][0],variable=task,value=no3[k][0],font=("Arial",12))
                    r10.grid(row=k+1,column=4,sticky='w')
                    lis2.append((r10,no3[k][0]))
        #Adding Tasks
        def add():
            e = Entry(can,width=50,font=("Arial",12))
            e.grid(row=len(lis)+3,column=0)
            def save():
                if len(e.get())==0:
                    messagebox.showerror("Error","Enter a Value")
                else:
                    #q = "insert into to_do values('{}')".format(e.get())
                    q = "insert into {} values('{}',NULL,NULL)".format(user,e.get())
                    c.execute(q)
                    mycon.commit()
                    #Creating a Radiobutton for the added task
                    e.destroy()
                    b1.destroy()
                    bb1.destroy()
                    rearrange()
            def cancel():
                e.destroy()
                bb1.destroy()
                b1.destroy()
                rearrange()
            b1 = Button(can,text="Save",command=save,padx=20,pady=5,font=("Arial",12))
            b1.grid(row=len(lis)+4,column=0)
            bb1 = Button(can,text="Cancel",command=cancel,padx=20,pady=5,font=("Arial",12))
            bb1.grid(row=len(lis)+3,column=1)
            
        #Shifting the tasks
        def shift():
            if len(lis)==0:
                but.configure(state=DISABLED)
            else:
                but.configure(state=ACTIVE)
                for i in range(len(lis)):
                    if lis[i][1]==task.get():       #Going through every data of the list and updating the record we want
                        #q2 = "insert into doing values('{}')".format(task.get())           #Ek jagah insert kiya toh dusri jagah delete bhi karna padega na
                        #q3 = "delete from to_do where to_do = '{}'".format(task.get())
                        q2 = "update {} set doing = '{}' where todo = '{}'".format(user,task.get(),task.get())
                        q3 = "update {} set todo = NULL where todo = '{}'".format(user,task.get())
                        c.execute(q2)
                        c.execute(q3)
                        mycon.commit()
                        break
                rearrange()
                    
        #Updating the tasks
        def update():
            for i in range(len(lis)):
                if lis[i][1]==task.get():           #Going through every data of the list and updating the record we want
                    e1 = Entry(can,width=50,font=("Arial",12))
                    e1.grid(row=i+2,column=0,sticky='w')
                    e1.insert(0,task.get())
                    x = lis[i][0]
                    def save1():
                        #q2 = "update to_do set To_Do = '{}' where To_Do = '{}'".format(e1.get(),task.get())
                        q2 = "update {} set todo = '{}' where todo = '{}'".format(user,e1.get(),task.get())
                        c.execute(q2)
                        mycon.commit()
                        x.destroy()
                        #Destroying buttons which are no more of use
                        e1.destroy()
                        rearrange()
                        b2.destroy()
                        
                    b2 = Button(can,text="save",command=save1,padx=10,pady=5,font=("Arial",12))
                    b2.grid(row=i+2,column=1)

        but3 = Button(can,text="Update",command=update,padx=20,pady=5,font=("Arial",12))
        but3.grid(row=28,column=0)  
        but = Button(can,text="-->",command=shift,padx=20,pady=5,font=("Consolas",12))
        but.grid(row=29,column=0)
        b =Button(can,text="Add Task",command=add,padx=20,pady=5,font=("Arial",12))
        b.grid(row=1,column=0,sticky='n')

        line = Label(can,text="_________________________________________________")
        line.grid(row=30,column=0)

        lab1 = Label(can,text='                        ')
        lab1.grid(row=0,column=1)

        # Doing Column
        lab2 = Label(can,text="Doing Task",font=("Arial",15))
        lab2.grid(row=0,column=2,sticky='n')
        #Recovering Data from Doing table
        #q3 = "select * from doing"
        q3 = "select doing from {}".format(user)
        c.execute(q3)
        dat1 = c.fetchall()
        mycon.commit()
        a2=[]
        for i in range(len(dat1)):
            if dat1[i][0] != None:
                a2.append(dat1[i])
        for i in range(len(a2)):
                r4 = Radiobutton(can,text=a2[i][0],variable=task,value=a2[i][0],font=("Arial",12))
                lis1.append((r4,a2[i][0]))
                r4.grid(row=i+1,column=2,sticky='w')

        def shift1():
            l1 = len(lis1)
            for i in range(l1):
                if lis1[i][1]==task.get():
                    #q5 = "insert into done values('{}')".format(task.get())
                    #q6 = "delete from doing where doing='{}'".format(task.get())
                    q5 = "update {} set done = '{}' where doing = '{}'".format(user,task.get(),task.get())
                    q6 = "update {} set doing = NULL where doing = '{}'".format(user,task.get())
                    c.execute(q5)
                    c.execute(q6)
                    mycon.commit()
                    break
            rearrange()
        def shift2():
            l2 = len(lis1)
            for i in range(l2):
                if lis1[i][1]==task.get():
                    #q7= "insert into to_do values('{}')".format(task.get())
                    #q8= "delete from doing where doing = '{}'".format(task.get())
                    q7 = "update {} set todo = '{}' where doing = '{}'".format(user,task.get(),task.get())
                    q8 = "update {} set doing = NULL where doing = '{}'".format(user,task.get())
                    c.execute(q7)
                    c.execute(q8)
                    mycon.commit()
                    break
            rearrange()

        but1 = Button(can,text='-->',command=shift1,padx=20,pady=5,font=("Consolas",12))
        but1.grid(row=29,column=2)
        but17 = Button(can,text='<--',command=shift2,padx=20,pady=5,font=("Consolas",12))
        but17.grid(row=28,column=2)
        line1 = Label(can,text="_________________________________________________")
        line1.grid(row=30,column=2)

        space = Label(can,text='                        ')
        space.grid(row=0,column=3)

        #Done Column
        lab3 = Label(can,text="Done Tasks",font=("Arial",15))
        lab3.grid(row=0,column=4,sticky='n')
        #q4 = "select * from done"
        q4 = "select done from {}".format(user)
        c.execute(q4)
        dat2 = c.fetchall()
        mycon.commit()
        a3 = []
        for i in range(len(dat2)):
            if dat2[i][0]:
                a3.append(dat2[i])
        for i in range(len(a3)):
                r5 = Radiobutton(can,text=a3[i][0],variable=task,value=a3[i][0],font=("Arial",12))
                lis2.append((r5,a3[i][0]))
                r5.grid(row=i+1,column=4,sticky='w')
        def delete():
            for i in range(len(lis2)):
                if lis2[i][1]==task.get():
                    #q5 = "delete from done where done='{}'".format(task.get())
                    q5 = "delete from {} where done = '{}'".format(user,task.get())
                    c.execute(q5)
                    mycon.commit()
                    break
            rearrange()
        def shift3():
            l4 = len(lis2)
            for i in range(l4):
                if lis2[i][1]==task.get():
                    #q7 = "insert into doing values('{}')".format(task.get())
                    #q8 = "delete from done where done= '{}'".format(task.get())
                    q7 = "update {} set doing = '{}' where done = '{}'".format(user,task.get(),task.get())
                    q8 = "update {} set done = NULL where done = '{}'".format(user,task.get())
                    c.execute(q7)
                    c.execute(q8)
                    mycon.commit()
                    break
            rearrange()
                
        but7 = Button(can,text="<--",command=shift3,padx=20,pady=5,font=("Consolas",12))
        but7.grid(row=29,column=4)
        but2 = Button(can,text="Delete",command=delete,padx=20,pady=5,font=("Arial",12))
        but2.grid(row=28,column=4)
        line2 = Label(can,text="_________________________________________________")
        line2.grid(row=30,column=4)
        Lbl1010 = Label(root,text="",font=("Arial",15))
        Lbl1010.pack()
        exite = Button(root,text="EXIT",command=root.destroy,padx=20,pady=5,font=("Arial",12))
        exite.pack()
        def back():
            backe.destroy()
            can.destroy()
            stlogin()
            but12 = Button(can1,text="Login",command = login)
            but12.grid(row=3,column=0)
            exite.destroy()
            but11 = Button(can1,text="Reg",command=reg)
            but11.grid(row=4,column=0)
        backe = Button(root,text="Back",command=back,font=("Arial",12))
        backe.pack()

        #Key points
        #top = Toplevel()
        #lab10 = Label(top,text='KEY POINTERS',font=("Arial",15))
        #lab10.pack()

        def add1():
            e = Entry(can,width=50,font=("Arial",12))
            e.grid(row=len(lis)+3,column=0)
            def save():
                if len(e.get())==0:
                    messagebox.showerror("Error","Enter a Value")
                else:
                    q = "insert into to_do values('{}')".format(e.get())
                    c.execute(q)
                    mycon.commit()
                    #Creating a Radiobutton for the added task
                    e.destroy()
                    b1.destroy()
                    rearrange()
            b1 = Button(can,text="Save",command=save,padx=20,pady=5,font=("Arial",12))
            b1.grid(row=len(lis)+5,column=0)

but12 = Button(can1,text="Login",command = login)
but12.grid(row=3,column=0)
root.mainloop()

