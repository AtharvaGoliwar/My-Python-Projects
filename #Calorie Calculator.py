#Calorie Calculator
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import date
import mysql.connector
mycon = mysql.connector.connect(host="localhost",username="root",password="abc123",database="calorie")
c = mycon.cursor()
if mycon.is_connected():
    print("GG")
root= Tk()
root.title("Calorie Calculator")

lab = Label(root,text="Calorie Calculator",font=("Arial",20))
lab.pack()
can = Canvas(root)
can.pack()
def but(t,meta):
    top = Toplevel(root)
    lab = Label(top,text="Activity: ")
    lab.grid(row=0,column=0)
    lab1 = Label(top,text=t)
    lab1.grid(row=0,column=1)
    lab2 = Label(top,text="Enter Your Weight: ")
    lab2.grid(row=1,column=0)
    e1 = Entry(top,width=7)
    e1.grid(row=1,column=1)
    lab3 = Label(top,text="Kg")
    lab3.grid(row=1,column=2)
    lab4 = Label(top,text="",font=("Arial",12))
    lab4.grid(row=2,column=0)
    hour = StringVar()
    hour.set("0")
    min = StringVar()
    min.set("0")
    lab5 = Label(top,text="Select Time (Hours) of workout: ")
    lab5.grid(row=3,column=0)
    op1 = OptionMenu(top,hour,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24')
    op1.grid(row=3,column=1)
    lab6 = Label(top,text="Hour")
    lab6.grid(row=3,column=2)
    lab7 = Label(top,text="Select time (minutes) of workout: ")
    lab7.grid(row=4,column=0)
    op2 = OptionMenu(top,min,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
    op2.grid(row=4,column=1)
    lab8 = Label(top,text="minutes")
    lab8.grid(row=4,column=2)

    lab9 = Label(top,text="MET Value: ")
    lab9.grid(row=5,column=0)
    lab10 = Label(top,text=meta)
    lab10.grid(row=5,column=1)
    lab11 = Label(top,text="",font=("Arial",15))
    lab11.grid(row=7,column=0)

    def calculate():
        if e1.get()=="":
            messagebox.showerror("Calorie Tracker","Input a correct value")
        else:
            cal = float(meta)*3.5*(float(e1.get()))*((int(hour.get())*60) + int(min.get()))
            ans = cal/200
            lab11.configure(text="{} CAL".format(ans))

        def save():
            d = str(date.today())
            q1 = "insert into d0 values('{}',{},'{}')".format(t,ans,d)
            c.execute(q1)
            mycon.commit()
            q2 = "select day from d0"
            c.execute(q2)
            dat2 = c.fetchall()
            for i in range(len(dat2)):
                if dat2[i][0] != d:
                    q3 = "delete from d0 where day != '{}'".format(d)
                    c.execute(q3)
                    mycon.commit()
            but3.configure(state=DISABLED)


        but3 = Button(top,text="Save Info",command=save)
        but3.grid(row=6,column=1)
        
        #messagebox.showinfo("CALORIE CALCULATOR","THIS WILL BURN {} KCAL".format(ans))

    but1 = Button(top,text="Calculate",command=calculate)
    but1.grid(row=6,column=0)

def grid():
    but1 = Button(can,text="Bicycling (leisure)",height=2,width=20,command= lambda: but(but1["text"],8.0))
    but1.grid(row=0,column=0)
    but2 = Button(can,text="Bicycling (Vigorous)",height=2,width=20,command= lambda: but(but2["text"],14.0))
    but2.grid(row=0,column=1)
    but3 = Button(can,text="Jumping Rope",height=2,width=20,command= lambda: but(but3["text"],12.3))
    but3.grid(row=0,column=2)
    but4 = Button(can,text="Yoga",height=2,width=20,command= lambda: but(but4["text"],2.5))
    but4.grid(row=0,column=3)
    but5 = Button(can,text="Home Activities",height=2,width=20,command= lambda: but(but5["text"],3.5))
    but5.grid(row=1,column=0)
    but6 = Button(can,text="Running (9 kmph)",height=2,width=20,command= lambda: but(but6["text"],9.8))
    but6.grid(row=1,column=1)
    but7 = Button(can,text="Running (18 kmph)",height=2,width=20,command= lambda: but(but7["text"],20.3))
    but7.grid(row=1,column=2)
    but8 = Button(can,text="Golf",height=2,width=20,command= lambda: but(but8["text"],4.3))
    but8.grid(row=1,column=3)
    but9 = Button(can,text="Tennis",height=2,width=20,command= lambda: but(but9["text"],7.8))
    but9.grid(row=2,column=0)
    but10 = Button(can,text="Basketball",height=2,width=20,command= lambda: but(but10["text"],8.5))
    but10.grid(row=2,column=1)
    but11 = Button(can,text="Brisk Walk",height=2,width=20,command= lambda: but(but11["text"],4.3))
    but11.grid(row=2,column=2)
    but12 = Button(can,text="Swimming",height=2,width=20,command= lambda: but(but12["text"],6.9))
    but12.grid(row=2,column=3)
    but13 = Button(can,text="Hiking",height=2,width=20,command= lambda: but(but13["text"],7.3))
    but13.grid(row=3,column=0)
    but14 = Button(can,text="Sitting",height=2,width=20,command= lambda: but(but14["text"],1.3))
    but14.grid(row=3,column=1)
    but15 = Button(can,text="Standing",height=2,width=20,command= lambda: but(but15["text"],1.9))
    but15.grid(row=3,column=2)
    but16 = Button(can,text="Aerobics",height=2,width=20,command= lambda: but(but16["text"],5.8))
    but16.grid(row=3,column=3)

def view():
    labs = []
    vals = []
    cnt = 0
    q3 = "select day from d0"
    c.execute(q3)
    dat3 = c.fetchall()
    day = str(date.today())
    if dat3[0][0] != day:
        q4 = "delete from d0 where day != '{}'".format(day)
        c.execute(q4)
        mycon.commit()
    q1 = "select exercise from d0"
    c.execute(q1)
    dat1 = c.fetchall()
    q2 = "select calories from d0"
    c.execute(q2)
    dat2 = c.fetchall()
    for i in range(len(dat1)):
        labs.append(dat1[i][0])
    for j in range(len(dat2)):
        vals.append(dat2[j][0])
        cnt+=int(dat2[j][0])

    plt.pie(vals,labels=labs,shadow=True)
    plt.title("Total Cal: {}".format(cnt))
    plt.show()
    
    return
def start():
    global can
    can.destroy()
    can = Canvas(root)
    can.pack()
    but2 = Button(can,text="Calculate",command=grid)
    but2.grid(row=0,column=0)
    but3 = Button(can,text="View",command=view)
    but3.grid(row=0,column=1)
start()
but1 = Button(root,text="Back",command=start)
but1.pack(anchor="n")

root.mainloop()