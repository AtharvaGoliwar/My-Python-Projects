from tkinter.tix import DECREASING
from urllib.request import urlopen
import webbrowser
from tkinter import *
import mysql.connector
mycon = mysql.connector.connect(host='localhost',username='root',passwd='abc123',database='tkinter_projects')
c=mycon.cursor()



'''a = [15,5,20,8,11,1,4]
x = sorted(a)
z=len(x)*(-1)
y= x[-1:z-1:-1]
print(x)
print(y)
l = 'open www.google.com'
a = l.split(' ')
print(a)
def x():
    global abc
    abc=10
    print(abc)
x()
if abc==10:
    print('gg')'''


root = Tk()
'''can = Canvas(root,height=300,width=300)
can.grid(row=10,column=5)
x=0
y=0
circle = can.create_oval(x,y,x+50,y+50)
def right(event):
    x=10
    y=0
    can.move(circle,x,y)
root.bind("d",right)

Fr = Frame(root)
Fr.grid(row=11,column=5)
Label(Fr,text="").pack(anchor='center')
print(Fr)
x = int(input("Bla"))
if x==1:
    Label(Fr,text="Atharva is pro").pack(anchor='center'''


'''q1 = 'select * from batch_1'
c.execute(q1)
dat1 = c.fetchall()'''

can1 = Canvas(root)
can1.pack()
e1 = Entry(can1,width=20)
e1.pack()
def login():
    x = e1.get()
    can1.destroy()
    q1 = 'select done from {}'.format(x)
    c.execute(q1)
    dat1 = c.fetchall()
    print(dat1)
    for i in range(len(dat1)):
        if dat1[i][0] != None:
            print(dat1[i][0])
            
but1 = Button(can1,text="Login",command=login)
but1.pack()

var = StringVar()
a = Checkbutton(can1,text="hello",variable=var)
a.pack()
def but12():
    print(var.get())
but = Button(root,text='x',command=but12)
but.pack()


root.mainloop()