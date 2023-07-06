#Calorie Counter using class
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import date,timedelta
import pickle
import mysql.connector
mycon = mysql.connector.connect(host="localhost",username="root",passwd = "abc123",database="abc")
c = mycon.cursor()
root = Tk()
root.title("Calorie Tracker")

class Calorie():
    def __init__(self):
        lab = Label(root,text="Calorie Counter",font=("Arial",20))
        lab.pack()
        self.can = Canvas(root)
        self.can.pack()
        but1 = Button(root,text="Calculate",height=2,width=20,command=self.grid)
        but1.pack()
        but2 = Button(root,text="View",height=2,width=20,command=self.view)
        but2.pack()
    def grid(self):
        but1 = Button(self.can,text="Bicycling (leisure)",height=2,width=20,command= lambda: self.but(but1["text"],8.0))
        but1.grid(row=0,column=0)
        but2 = Button(self.can,text="Bicycling (Vigorous)",height=2,width=20,command= lambda: self.but(but2["text"],14.0))
        but2.grid(row=0,column=1)
        but3 = Button(self.can,text="Jumping Rope",height=2,width=20,command= lambda: self.but(but3["text"],12.3))
        but3.grid(row=0,column=2)
        but4 = Button(self.can,text="Yoga",height=2,width=20,command= lambda: self.but(but4["text"],2.5))
        but4.grid(row=0,column=3)
        but5 = Button(self.can,text="Home Activities",height=2,width=20,command= lambda: self.but(but5["text"],3.5))
        but5.grid(row=1,column=0)
        but6 = Button(self.can,text="Running (9 kmph)",height=2,width=20,command= lambda: self.but(but6["text"],9.8))
        but6.grid(row=1,column=1)
        but7 = Button(self.can,text="Running (18 kmph)",height=2,width=20,command= lambda: self.but(but7["text"],20.3))
        but7.grid(row=1,column=2)
        but8 = Button(self.can,text="Golf",height=2,width=20,command= lambda: self.but(but8["text"],4.3))
        but8.grid(row=1,column=3)
        but9 = Button(self.can,text="Tennis",height=2,width=20,command= lambda: self.but(but9["text"],7.8))
        but9.grid(row=2,column=0)
        but10 = Button(self.can,text="Basketball",height=2,width=20,command= lambda: self.but(but10["text"],8.5))
        but10.grid(row=2,column=1)
        but11 = Button(self.can,text="Brisk Walk",height=2,width=20,command= lambda: self.but(but11["text"],4.3))
        but11.grid(row=2,column=2)
        but12 = Button(self.can,text="Swimming",height=2,width=20,command= lambda: self.but(but12["text"],6.9))
        but12.grid(row=2,column=3)
        but13 = Button(self.can,text="Hiking",height=2,width=20,command= lambda: self.but(but13["text"],7.3))
        but13.grid(row=3,column=0)
        but14 = Button(self.can,text="Sitting",height=2,width=20,command= lambda: self.but(but14["text"],1.3))
        but14.grid(row=3,column=1)
        but15 = Button(self.can,text="Standing",height=2,width=20,command= lambda: self.but(but15["text"],1.9))
        but15.grid(row=3,column=2)
        but16 = Button(self.can,text="Aerobics",height=2,width=20,command= lambda: self.but(but16["text"],5.8))
        but16.grid(row=3,column=3)

    def but(self,act,meta):
        # Creating inputs for users to choose and eventually calculate calories 
        self.meta = meta
        self.activity = act
        top = Toplevel()
        lab = Label(top,text="Activity: ")
        lab.grid(row=0,column=0)
        lab1 = Label(top,text=act)
        lab1.grid(row=0,column=1)
        self.lab2 = Label(top,text="Enter Your Weight: ")
        self.lab2.grid(row=1,column=0)
        self.e1 = Entry(top,width=7)
        self.e1.grid(row=1,column=1)
        lab3 = Label(top,text="Kg")
        lab3.grid(row=1,column=2)
        lab4 = Label(top,text="",font=("Arial",12))
        lab4.grid(row=2,column=0)
        self.hour = StringVar()
        self.hour.set("0")
        self.min = StringVar()
        self.min.set("0")
        lab5 = Label(top,text="Select Time (Hours) of workout: ")
        lab5.grid(row=3,column=0)
        op1 = OptionMenu(top,self.hour,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24')
        op1.grid(row=3,column=1)
        lab6 = Label(top,text="Hour")
        lab6.grid(row=3,column=2)
        lab7 = Label(top,text="Select time (minutes) of workout: ")
        lab7.grid(row=4,column=0)
        op2 = OptionMenu(top,self.min,'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60')
        op2.grid(row=4,column=1)
        lab8 = Label(top,text="minutes")
        lab8.grid(row=4,column=2)

        lab9 = Label(top,text="MET Value: ")
        lab9.grid(row=5,column=0)
        self.lab10 = Label(top,text=meta)
        self.lab10.grid(row=5,column=1)
        self.lab11 = Label(top,text="",font=("Arial",15))
        self.lab11.grid(row=7,column=0)

        self.but1 = Button(top,text="Calculate",command=self.calculate)
        self.but1.grid(row=6,column=0)
        self.but2 = Button(top,text="Save info",command=self.save)
        self.but2.grid(row=6,column=1)

    def calculate(self):
        if self.e1.get()=="":
            messagebox.showerror("Calorie Tracker","Enter a valid input")
        try:
            self.cal = float(self.meta)*3.5*(float(self.e1.get()))*((int(self.hour.get())*60) + int(self.min.get()))
            self.ans = self.cal/200
            self.lab11.configure(text="{} CAL".format(self.ans))
        except:
            messagebox.showerror("Calorie Tracker","Enter a valid input")                     ##Here Using try & except to show message if any type of error occurs (which the code does not want)
        
    def save(self):
        d = str(date.today())        # Current Date using Datetime module

        #Inserting workout data in Today Workout table
        q1 = "insert into today values('{}',{},'{}')".format(self.activity,self.ans,d)
        c.execute(q1)
        mycon.commit()

        #Deleting workout data of any previous days from today workout table
        q2 = "select date from today"
        c.execute(q2)
        dat2 = c.fetchall()
        for i in range(len(dat2)):
                if dat2[i][0] != d:
                    q3 = "delete from today where date != '{}'".format(d)
                    c.execute(q3)
                    mycon.commit()

        #Inserting / Updating Data in the Bar graph Table
        q4 = "select sum(cal) from today"
        c.execute(q4)
        dat4 = c.fetchall()
        q5 = "select date from cals"
        c.execute(q5)
        dat5 = c.fetchall()
        for i in range(len(dat5)):
            if (d,) in dat5:
                q6 = "update cals set cal = {} where date = '{}'".format(dat4[0][0],d)
                c.execute(q6)
                mycon.commit()
            else:
                q7 = "insert into cals values('{}',{})".format(d,dat4[0][0])
                c.execute(q7)
                mycon.commit()
        
        # Creating List of past 5 dates to check whether those dates are only in the tble or not
        past_dates = []
        for i in range(5):
            x = str(date.today() - timedelta(days=i))
            past_dates.append(x)

        q8 = "select date from cals"
        c.execute(q8)
        dat8 = c.fetchall()
        for i in range(len(dat8)):
            if dat8[i][0] not in past_dates:
                q9 = "delete from cals where date = '{}'".format(dat8[i][0])         ##If a particular date is not in list, the record is deleted and table is updated
                c.execute(q9)
                mycon.commit()        

        self.but2.configure(state=DISABLED)     ##Can Save the info only once

    def view(self):
        #labs=["basketball","aerobics","running","walking"]
        #vals=[2875.7,870.4,1200,500]
        labs=[]
        vals=[]
        cnt=0

        #Deleting the Data stored from previous dates
        q1 = "select date from today"
        c.execute(q1)
        dat1 = c.fetchall()
        day1 = str(date.today())
        if dat1[0][0] != day1:
            q2 = "delete from today where date != '{}'".format(day1)
            c.execute(q2)
            mycon.commit()
        
        #Creating Lists to plot the pie-chart
        q3 = "select activity from today"
        c.execute(q3)
        dat3 = c.fetchall()
        q4 = "select cal from today"
        c.execute(q4)
        dat4 = c.fetchall()
        for i in range(len(dat3)):
            labs.append(dat3[i][0])
        for j in range(len(dat4)):
            vals.append(dat4[j][0])
            cnt+=int(dat4[j][0])
        plt.subplot(2,1,1)                      ## Plotting of Pie-Chart
        plt.pie(vals,labels=labs,shadow=True)
        plt.title("Total Cal: {} Cal".format(cnt))

        #Plotting of Bar Graph of past 5 days workout
        lab1 = []
        val1 = []
        q5 = "select * from cals"
        c.execute(q5)
        dat5 = c.fetchall()
        print((str(date.today())),)
        for i in range(len(dat5)):
            lab1.append(dat5[i][0])
            val1.append(dat5[i][1])
        print(lab1)
        print(val1)
        
        plt.subplot(2,1,2)
        plt.bar(val1,lab1)
        plt.xlabel("Dates")
        plt.ylabel("Calories")

        plt.show()

Calorie()
root.mainloop()