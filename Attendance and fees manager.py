from tkinter import *
root = Tk()
import mysql.connector
mycon = mysql.connector.connect(host='localhost',username='root',passwd='abc123',database='savi')
c=mycon.cursor()

def add():
    top1 = Toplevel(root)
    Lbl3 = Label(top1, text='Enter your Name :',font=('Arial',12))
    Lbl3.grid(row=2,column=0)
    e= Entry(top1, width=30,font=('Arial',12))
    e.grid(row=2,column=1)
    Lbl4 = Label(top1, text='Enter your Date of Birth (DD/MM/YYYY) :',font=('Arial',12))
    Lbl4.grid(row=3,column=0)
    e1= Entry(top1, width=5,font=('Arial',12))
    e1.grid(row=3,column=1)
    Lbl22 = Label(top1,text='/',font=("Arial",12))
    Lbl22.grid(row=3,column=2)
    e3 = Entry(top1, width=5,font=('Arial',12))
    e3.grid(row=3,column=3)
    Lbl22 = Label(top1,text='/',font=("Arial",12))
    Lbl22.grid(row=3,column=4)
    e4 = Entry(top1,width=5,font=("Arial",12))
    e4.grid(row=3,column=5)
    Lbl18 = Label(top1,text='Select Your Gender',font=('Arial',12))
    Lbl18.grid(row=4,column=0)
    
    Gen = StringVar()
    Gen.set('M')
    r1 = Radiobutton(top1,text='Male',variable = Gen,value='M',font=('Arial',12))
    r1.grid(row=4,column=1)
    r2 = Radiobutton(top1,text='Female',variable = Gen,value='F',font=('Arial',12))
    r2.grid(row=5,column=1)
    r3 = Radiobutton(top1,text='Other',variable = Gen,value='O',font=('Arial',12))
    r3.grid(row=6,column=1)
        #e7 = Entry(top1,width)
        #e7.grid(row=4,column=1)
    Lbl19 = Label(top1,text='State you Reside in:',font=('Arial',12))
    Lbl19.grid(row=7,column=0)

    state = StringVar()
    state.set("Delhi")
    s1 = OptionMenu(top1,state,"Delhi","Maharashtra","Tamil Nadu","Gujrat","Karnataka","USA","Qatar")
    s1.grid(row=7,column=1)
        #e8 = Entry(top1,width=10,font=('Arial',12))
        #e8.grid(row=7,column=1)
    Lbl20 = Label(top1,text='Enter your Phone Number:',font=('Arial',12))
    Lbl20.grid(row=8,column=0)
    e9 = Entry(top1,width=15,font=('Arial',12))
    e9.grid(row=8,column=1)

    batch= StringVar()
    batch.set("Select Batch")
    s2 = OptionMenu(top1,batch,"Batch_1","Batch_2","Batch_3","USA_Batch","Qatar_Batch")
    s2.grid(row=9,column=1)
    Lbl21 = Label(top1,text="Select Batch: ")
    Lbl21.grid(row=9,column=0)

    def submit():
                a = e1.get()
                b = e3.get()
                d=e4.get()
                dob = "{}/{}/{}".format(a,b,d)
                '''while True:
                        if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
                                if a>0 and a<32:
                                        break
                               
                                else:
                                        e1.delete(0,END)
                                        e3.delete(0,END)
                                        e4.delete(0,END)
                                        print("enter dob again")
                        if b==2 or b==4 or b==6 or b==9 or b==11:
                                if a>0 and a<31:
                                        break
                               
                                else:
                                        e1.delete(0,END)
                                        e3.delete(0,END)
                                        e4.delete(0,END)
                                        print("enter dob again")'''
                x = "insert into {} values('{}','{}','{}','{}','{}')".format(batch.get(),e.get(),dob,Gen.get(),state.get(),e9.get())
                c.execute(x)
                mycon.commit()
                
                Lbl5= Label(top1, text='Successfully Registered')
                Lbl5.grid(row=12,column=0)
    but2 = Button(top1,text="Add",command=submit)
    but2.grid(row=11,column=0)


def attendance():
        def batch(x):
                top3 = Toplevel(root)
                q1 = "select Name from batch_{}".format(x)
                c.execute(q1)
                dat = c.fetchall()
                
                for i in range(len(dat)):
                        lab = Label(top3,text=dat[i])
                        lab.grid(row=i,column=0)
                        att = StringVar()
                        att.set("")
                        r1 = Radiobutton(top3,text="P",variable=att,value="P")
                        r1.grid(row=i,column=1)
                        r2 = Radiobutton(top3,text="A",variable=att,value="A")
                        r2.grid(row=i,column=2)

                        but4 = Button(top3,text='save')
                        but4.grid(row=i,column=3)
                
        lab = Label(root,text="Enter Date (DD/MM/YYYY): ")
        lab.grid(row=1,column=0)
        e1 = Entry(root,width=20)
        e1.grid(row=1,column=1)              
        but3 = Button(root,text="Batch_1",command=lambda: batch(1))
        but3.grid(row=2,column=0)
but1 = Button(root,text='Add Student',command=add)
but1.grid(row=0,column=0)
but2 = Button(root,text="Attendance",command=attendance)
but2.grid(row=0,column=1)


root.mainloop()