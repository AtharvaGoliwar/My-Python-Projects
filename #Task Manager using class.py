#Task Manager using class
from tkinter import *
from tkinter import messagebox
import pickle

from requests import delete

class task_manager():
    def __init__(self):
        self.root = Tk()
        self.root.title("Task Manager using class")
        self.basic_structure()
        self.root.mainloop()
        
    def basic_structure(self):
        lab1 = Label(self.root,text="MY TASK MANAGER",font=("Arial",20))
        lab1.pack()
        self.can = Canvas(self.root)
        self.can.pack()
        lab2 = Label(self.can,text="To Do",font=("Arial",15))
        lab2.grid(row=0,column=0)
        self.todoread()
        self.showtodo()
        self.doingread()
        self.showdoing()
        self.doneread()
        self.showdone()
        but = Button(self.can,text="Add Task",command=self.add,height=2,width=10,font=("Arial",10))
        but.grid(row=30,column=0)
        but1 = Button(self.can,text="Update",command=self.update,width=10,height=2,font=("Arial",10))
        but1.grid(row=31,column=0)
        labb = Label(self.can,text="                       ",font=("Arial",15))
        labb.grid(row=0,column=1)
        lab3 = Label(self.can,text="Doing",font=("Arial",15))
        lab3.grid(row=0,column=2)
        labb10 = Label(self.can,text="                                 ",font=("Arial",15))
        labb10.grid(row=0,column=3)
        lab4 = Label(self.can,text="Done",font=("Arial",15))
        lab4.grid(row=0,column=4)
        but2 = Button(self.can,text="Delete",command=self.delete_done,height=2,width=10)
        but2.grid(row=31,column=4)
        but3 = Button(self.can,text="-->",command= lambda: self.shift('todo.dat','doing.dat'),font=("Consolas",10),height=2,width=10)
        but3.grid(row=32,column=0)
        but4 = Button(self.can,text='<--',command= lambda: self.shift('doing.dat','todo.dat'),font=("Consolas",10),height=2,width=10)
        but4.grid(row=30,column=2)
        but5 = Button(self.can,text='-->',command= lambda: self.shift('doing.dat','done.dat'),font=("Consolas",10),height=2,width=10)
        but5.grid(row=31,column=2)
        but6= Button(self.can,text='<--',command= lambda: self.shift('done.dat','doing.dat'),font=("Consolas",10),height=2,width=10)
        but6.grid(row=30,column=4)

        but11 = Button(self.root,text="Exit",height=2,width=10,font=("Arial",12),command=self.root.destroy)
        but11.pack()


    def todoread(self):
        self.read_todo = []
        f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','rb')
        try:
            while True:
                dat = pickle.load(f)
                self.read_todo.append(dat)
                print(dat)
        except EOFError:
            f.close()

    def showtodo(self):
        self.task = StringVar()
        self.task.set("")
        self.rcheck = []
        for i in self.read_todo:
            r1 = Radiobutton(self.can,text=i[0],variable=self.task,value=i[0],font=("Arial",10))
            self.rcheck.append((r1,i[0]))
            r1.grid(row=self.read_todo.index(i)+1,column=0,sticky='w')
    def add(self):
        self.e = Entry(self.can,width=30,font=("Arial",10))
        self.e.grid(row = len(self.rcheck)+1,column=0)
        self.savebut = Button(self.can,text="Save",command=self.save)
        self.savebut.grid(row=len(self.rcheck)+2 , column=0)
        self.cancelbut = Button(self.can,text="Cancel",command=self.cancel)
        self.cancelbut.grid(row=len(self.rcheck)+1,column=1)
        
    def save(self):
        if self.e.get()=="":
            messagebox.showerror("Error","Enter a value")
        else:
            lis1 = []
            f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','ab')
            lis1.append(self.e.get())
            pickle.dump(lis1,f)
            f.close()
            self.savebut.destroy()
            self.e.destroy()
            self.cancelbut.destroy()
        
        self.rearrange()
    
    def cancel(self):
        self.e.destroy()
        self.savebut.destroy()
        self.cancelbut.destroy()
        self.rearrange()

    def update(self):
        self.todoread()
        f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','wb')
        r = self.task.get()
        for i in range(len(self.read_todo)):
            if [r]==self.read_todo[i]:
                self.rcheck[i][0].destroy()
                self.e1 = Entry(self.can,width=30,font=("Arial",10))
                self.e1.grid(row=i+1,column=0,sticky='w')
                self.e1.insert(0,self.rcheck[i][1])

            else:
                pickle.dump(self.read_todo[i],f)
        self.saveupbut = Button(self.can,text="Save",command=self.save_update)
        self.saveupbut.grid(row=i+1,column=1)
    
    def save_update(self):
        f1 = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','ab')
        pickle.dump([self.e1.get()],f1)
        self.e1.destroy()
        self.saveupbut.destroy()
        f1.close()
        self.rearrange()
        
        return
    
    def rearrange(self):
        self.todoread()
        self.doingread()
        self.doneread()
        #Destroy all the radiobuttons 
        for i in range(len(self.rcheck)):
            print("working")
            print(self.rcheck[i][0])
            self.rcheck[i][0].destroy()
        self.rcheck.clear()
        for rec in self.read_todo:
            r1 = Radiobutton(self.can,text=rec[0],variable=self.task,value=rec[0],font=("Arial",10))
            self.rcheck.append((r1,rec[0]))
            r1.grid(row=self.read_todo.index(rec)+1,column=0,sticky='w')

        for i in range(len(self.r1check)):
            print("working")
            self.r1check[i][0].destroy()
        self.r1check.clear()
        for rec in self.read_doing:
            r2 = Radiobutton(self.can,text=rec[0],variable=self.task,value=rec[0])
            self.r1check.append((r2,rec[0]))
            r2.grid(row=self.read_doing.index(rec)+1,column=2,sticky='w')

        for i in range(len(self.r2check)):
            print("working")
            self.r2check[i][0].destroy()
        self.r2check.clear()
        for rec in self.read_done:
            r3 = Radiobutton(self.can,text=rec[0],variable=self.task,value=rec[0])
            self.r2check.append((r3,rec[0]))
            r3.grid(row=self.read_done.index(rec)+1,column=4,sticky='w')


    def doingread(self):
        self.read_doing = []
        f =  open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\doing.dat','rb')
        try:
            while True:
                dat = pickle.load(f)
                self.read_doing.append(dat)
        except EOFError:
            f.close()

    def showdoing(self):
        self.r1check = []
        for i in self.read_doing:
            r2 = Radiobutton(self.can,text=i[0],variable=self.task,value=i[0])
            self.r1check.append((r2,i[0]))
            r2.grid(row=self.read_doing.index(i)+1,column=2,sticky='w')

    def doneread(self):
        self.read_done=[]
        f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\done.dat','rb')
        try:
            while True:
                dat = pickle.load(f)
                self.read_done.append(dat)
        except EOFError:
            f.close()
    
    def showdone(self):
        self.r2check=[]
        for i in self.read_done:
            r3 = Radiobutton(self.can,text=i[0],variable=self.task,value=i[0])
            self.r2check.append((r3,i[0]))
            r3.grid(row=self.read_done.index(i)+1,column=4,sticky='w')

    def delete_done(self):
        f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\done.dat','wb')
        lis=[]
        r = self.task.get()
        for rec in self.read_done:
            if rec==[r]:
                continue
            else:
                lis.append(rec)
                pickle.dump(rec,f)
        self.read_done.clear()
        for i in lis:
            self.read_done.append(i)

        f.close()

        self.rearrange()

    def delete_doing(self):
        f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\doing.dat','wb')
        lis=[]
        r = self.task.get()
        for rec in self.read_doing:
            if rec==[r]:
                continue
            else:
                lis.append(rec)
                pickle.dump(rec,f)
        self.read_doing.clear()
        for i in lis:
            self.read_doing.append(i)

        f.close()
        self.rearrange()
    
    def delete_todo(self):
        f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','wb')
        lis=[]
        r = self.task.get()
        for rec in self.read_todo:
            if rec==[r]:
                continue
            else:
                lis.append(rec)
                pickle.dump(rec,f)
        self.read_todo.clear()
        for i in lis:
            self.read_todo.append(i)

        f.close()
        self.rearrange()

    def shift(self,x,y):
        if self.task.get()=="":
            messagebox.showerror("TASK MANAGER","SELECT A TASK")
        else:
            r = self.task.get()
            if x=='todo.dat' and y=='doing.dat' and [r] in self.read_todo:
                self.delete_todo()
                self.read_doing.append([r])
                f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\{}'.format(y),'ab')
                pickle.dump([r],f)
                f.close()
                self.rearrange()
            elif x=='doing.dat' and y=='done.dat' and [r] in self.read_doing:
                self.delete_doing()
                self.read_done.append([r])
                f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\{}'.format(y),'ab')
                pickle.dump([r],f)
                f.close()
                self.rearrange()
            elif x=='done.dat' and y=='doing.dat' and [r] in self.read_done:
                self.delete_done()
                self.read_doing.append([r])
                f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\{}'.format(y),'ab')
                pickle.dump([r],f)
                f.close()
                self.rearrange()
            elif x=='doing.dat' and y=='todo.dat' and [r] in self.read_doing:
                self.delete_doing()
                self.read_todo.append([r])
                f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\{}'.format(y),'ab')
                pickle.dump([r],f)
                f.close()
                self.rearrange()

task_manager()

