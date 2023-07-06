
import mysql.connector
mycon = mysql.connector.connect(host = "localhost", user = "root", passwd = "abc123", database = "testing")
if mycon.is_connected():
        print('Successfully Connected')
c=mycon.cursor()

from tkinter import *
root = Tk()

x = 0
y = 0
lab = Label(root,text="GG")
lab.place(x=0,y=0)
lab2 = Label(root,text="O",font=("Arial",20))
lab2.place(x=20,y=20)
x1 = 2
y1=2
def left():
        global y
        y=y+100
        lab.place(x=x,y=y)
def moveball(a):
        global x1,y1
        if a==1:
                x1+=2
                y1+=2
        elif a==2:
                x1+=2
                y1 = y1-2
        lab2.place(x=x1,y=y1)
        root.after(50,lambda: moveball(1))
        if x1>200 and y1>200:
                root.after(100,lambda: moveball(2))

root.after(100,lambda: moveball(1))
but = Button(root,text="ok",command=left)
but.pack()
root.bind("s",lambda event: left())
root.mainloop()




