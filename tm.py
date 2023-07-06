from tkinter import *
import os
root=Tk()
def tmsql():
    os.startfile('C:/Users/Atharva Goliwar/Desktop/#Task Manager.py')
def tmfile():
    os.startfile('C:/Users/Atharva Goliwar/Desktop/#Task Manager with Binary File.py')
but1 = Button(root,text="Task Manager (My SQL)",command=tmsql)
but2 = Button(root,text="Task Manager (Binary File)",command=tmfile)
but1.pack()
but2.pack()
root.mainloop()