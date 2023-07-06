#Graph for Growth
from matplotlib import pyplot as plt
from tkinter import *
from tkinter import messagebox
import mysql.connector
mycon = mysql.connector.connect(host='localhost',user='root',passwd='abc123',database='trial')
c = mycon.cursor()
root = Tk()
def JEE():
    butt1.destroy()
    butt2.destroy()
    lab = Label(root,text="Graph for Marks",font=('Arial',20))
    lab.grid(row=0,column=0)
    lab1 = Label(root,text="Enter Name of Examination: ",font=("Arial",12))
    lab1.grid(row=1,column=0,sticky='w')
    e1 = Entry(root,width = 25,font=("Arial",12))
    e1.grid(row=1,column=1)
    lab3 = Label(root,text="",font=("Arial",5))
    lab3.grid(row=2,column=0)
    lab2 = Label(root,text="Enter Marks Scored: ",font=("Arial",12))
    lab2.grid(row=3,column=0,sticky='w')
    e2 = Entry(root,width = 25,font=("Arial",12))
    e2.grid(row=3,column=1)

    def save():
        if e1.get()=="" or e2.get()=="":
            messagebox.showerror("Graph","Enter Value")
        else:
            res = messagebox.askquestion("Graph","Are you sure you want to save this value?")
            print(res)
            if res=="yes":
                q1 = "insert into graph values('{}',{},'JEE')".format(e1.get(),e2.get())
                c.execute(q1)
                mycon.commit()
                e1.delete(0,END)
                e2.delete(0,END)
    lab4 = Label(root,text="",font=("Arial",5))
    lab4.grid(row=4,column=0)
    but1 = Button(root,text="Save",command=save,font=("Arial",12))
    but1.grid(row=5,column=0,sticky='w')

    def view():
        q1 = "select Name from graph where Exam = 'JEE'"
        c.execute(q1)
        dat1=c.fetchall()
        lis1 = []
        for i in range(len(dat1)):
            lis1.append(dat1[i][0])
            
        q2 = "select Marks from graph where Exam = 'JEE'"
        c.execute(q2)
        dat2=c.fetchall()
        lis2 = []
        for i in range(len(dat2)):
            lis2.append(dat2[i][0])
        print(lis1)
        print(lis2)
        plt.title("GROWTH CHECK")
        plt.plot(lis1,lis2)
        plt.xlabel("Name")
        plt.ylabel("Marks")
        plt.show()

    but2 = Button(root,text="View Graph",command=view,font=("Arial",12))
    but2.grid(row=6,column=0,sticky='w')

def BITSAT():
    butt1.destroy()
    butt2.destroy()
    lab = Label(root,text="Graph for Marks",font=('Arial',20))
    lab.grid(row=0,column=0)
    lab1 = Label(root,text="Enter Name of Examination: ",font=("Arial",12))
    lab1.grid(row=1,column=0,sticky='w')
    e1 = Entry(root,width = 25,font=("Arial",12))
    e1.grid(row=1,column=1)
    lab3 = Label(root,text="",font=("Arial",5))
    lab3.grid(row=2,column=0)
    lab2 = Label(root,text="Enter Marks Scored: ",font=("Arial",12))
    lab2.grid(row=3,column=0,sticky='w')
    e2 = Entry(root,width = 25,font=("Arial",12))
    e2.grid(row=3,column=1)
    def save():
        if e1.get()=="" or e2.get()=="":
            messagebox.showerror("Graph","Enter Value")
        else:
            res = messagebox.askquestion("Graph","Are you sure you want to save this value?")
            print(res)
            if res=="yes":
                q1 = "insert into graph values('{}',{},'BITSAT')".format(e1.get(),e2.get())
                c.execute(q1)
                mycon.commit()
                e1.delete(0,END)
                e2.delete(0,END)
    lab4 = Label(root,text="",font=("Arial",5))
    lab4.grid(row=4,column=0)
    but1 = Button(root,text="Save",command=save,font=("Arial",12))
    but1.grid(row=5,column=0,sticky='w')

    def view():
        q1 = "select Name from graph where Exam = 'BITSAT'"
        c.execute(q1)
        dat1=c.fetchall()
        lis1 = []
        for i in range(len(dat1)):
            lis1.append(dat1[i][0])
            
        q2 = "select Marks from graph where Exam = 'BITSAT'"
        c.execute(q2)
        dat2=c.fetchall()
        lis2 = []
        for i in range(len(dat2)):
            lis2.append(dat2[i][0])
        print(lis1)
        print(lis2)
        plt.title("GROWTH CHECK")
        plt.plot(lis1,lis2)
        plt.xlabel("Name")
        plt.ylabel("Marks")
        plt.show()

    but2 = Button(root,text="View Graph",command=view,font=("Arial",12))
    but2.grid(row=6,column=0,sticky='w')

butt1 = Button(root,text='JEE',font=("Arial",15),command=JEE)
butt1.grid(row=0,column=0)
butt2 = Button(root,text='BITSAT',font=("Arial",15),command=BITSAT)
butt2.grid(row=0,column=1)
root.mainloop()
