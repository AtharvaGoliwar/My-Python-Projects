#Task Manager Using Binary File
from tkinter import *
from tkinter import messagebox
import pickle

root=Tk()
root.title("Task Manager with Binary File")
lab1 = Label(root,text="MY TASK MANAGER",font = ("Arial",20))
lab1.pack()
scroll1 = Scrollbar(root,orient='horizontal')
scroll1.pack(side=BOTTOM,fill=X)
can = Canvas(root,xscrollcommand=scroll1.set)
can.pack()
scroll1.config(command=can.xview)
lab2 = Label(can,text='To Do',font=("Arial",15))
lab2.grid(row=0,column=0)

#reading the file
def todoread():
    global ch
    ch=[]
    f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','rb')
    try:
        while True:
            dat = pickle.load(f)
            ch.append(dat)
            print(dat)
    except EOFError:
        f.close()
    #print(ch)

todoread()

task = StringVar()
task.set("")
rcheck=[]
for i in ch:
    r1 = Radiobutton(can,text=i[0],variable=task,value=i[0],font=("Arial",10))
    rcheck.append((r1,i[0]))
    r1.grid(row=ch.index(i)+1,column=0,sticky='w')

def rearrange():
    todoread()
    doingread()
    doneread()
    for i in range(len(rcheck)):
        rcheck[i][0].destroy()
    rcheck.clear()
    for i in ch:
        r1 = Radiobutton(can,text=i[0],variable=task,value=i[0],font=("Arial",10))
        rcheck.append((r1,i[0]))
        r1.grid(row=ch.index(i)+1,column=0,sticky='w')

    for j in range(len(r1check)):
        r1check[j][0].destroy()
    r1check.clear()

    for i in ch1:
        r2 = Radiobutton(can,text=i[0],variable=task,value=i[0],font=("Arial",10))
        r1check.append((r2,i[0]))
        r2.grid(row=ch1.index(i)+1,column=2,sticky='w')

    for i in range(len(r2check)):
        r2check[i][0].destroy()
    r2check.clear()
    for i in ch2:
        r3 = Radiobutton(can,text=i[0],variable=task,value=i[0],font=("Arial",10))
        r2check.append((r3,i[0]))
        r3.grid(row=ch2.index(i)+1,column=4,sticky = 'w')

def add():
    e = Entry(can,width=30,font=("Arial",12))
    e.grid(row=len(rcheck)+1,column=0)
    def save():
        if len(e.get())==0:
            messagebox.showerror("Error","Enter a Value")
        else:
            lis1=[]
            f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','ab')
            lis1.append(e.get())
            #print(e.get())
            pickle.dump(lis1,f)
            f.close()
            todoread()
            butt.destroy()
            e.destroy()
            butt1.destroy()
            rearrange()
    def cancel():
        e.destroy()
        butt.destroy()
        butt1.destroy()
        rearrange()
    butt = Button(can,text="save",command=save,font=("Arial",10))
    butt.grid(row=len(rcheck)+2,column=0)
    butt1 = Button(can,text="Cancel",command=cancel,font=("Arial",10))
    butt1.grid(row=len(rcheck)+1,column=1)
    return

def delete():
    todoread()
    f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','wb')
    r= task.get()
    lis=[]
    for rec in ch:
        if rec==[r]:
            continue
        else:
            lis.append(rec)
            pickle.dump(rec,f)
    
    ch.clear()
    #print(ch)
    for i in lis:
        ch.append(i) 

    #print(ch)
    f.close()
    #todoread()
    rearrange()

def update():
    todoread()
    print(ch)
    f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','wb')
    r = task.get()
    lis=[]
    print([r])
    for i in range(len(ch)):
        if [r]==ch[i]:
            print(rcheck[i])
            rcheck[i][0].destroy()
            e = Entry(can,width=30,font=("Arial",10))
            e.grid(row=i+1,column=0,sticky='w')
            e.insert(0,rcheck[i][1])
            click = 0
            def save1():
                f1 = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\todo.dat','ab')
                lis.append(e.get())
                pickle.dump([e.get()],f1)
                e.destroy()
                but1.destroy()
                f1.close()
                rearrange()
            but1 = Button(can,text='save',command=save1,font=("Arial",10))
            but1.grid(row=i+1,column=1)

        else:
            lis.append(ch[i])
            pickle.dump(ch[i],f)
    
    f.close()
    #rearrange()

labb = Label(can,text='                        ',font=("Arial",10))
labb.grid(row=0,column=1)

lab3 = Label(can,text="Doing",font=("Arial",15))
lab3.grid(row=0,column=2)

def doingread():
    global ch1
    ch1=[]
    f =  open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\doing.dat','rb')
    try:
        while True:
            dat= pickle.load(f)
            ch1.append(dat)
            print(dat)
    except EOFError:
        f.close()
    #print(ch1)
doingread()
r1check=[]
#print(ch1)
for i in ch1:
    r2 = Radiobutton(can,text=i[0],variable=task,value=i[0],font=("Arial",10))
    r1check.append((r2,i[0]))
    r2.grid(row=ch1.index(i)+1,column=2,sticky='w')

def delete1():
    f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\doing.dat','wb')
    lis=[]
    r = task.get()
    for rec in ch1:
        if rec==[r]:
            continue
        else:
            lis.append(rec)
            pickle.dump(rec,f)
    ch1.clear()
    for i in lis:
        ch1.append(i)

    #print(ch1)
    f.close()
    #doingread()
    rearrange()

def delete2():
    f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\done.dat','wb')
    lis=[]
    r = task.get()
    for rec in ch2:
        if rec==[r]:
            continue
        else:
            lis.append(rec)
            pickle.dump(rec,f)
    ch2.clear()
    for i in lis:
        ch2.append(i)

    #print(ch2)
    f.close()
    #doneread()
    rearrange()

def shift(x,y):        ### Error in this function: there is no corelation between x and y here bcz of which todo ki value doing ke button se done mai update ho rahi hai
    if task.get()=="":
        messagebox.showinfo("TASK MANAGER","SELECT A TASK BEFORE SHIFTING")
    else:
        r = task.get()
        print([r])
        print(ch2)
        if x=='todo.dat' and y=='doing.dat' and [r] in ch:
            delete()
            ch1.append([r])
            f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\{}'.format(y),'ab')
            pickle.dump([r],f)
            f.close()
            rearrange()
        elif x=='doing.dat' and y=='done.dat' and [r] in ch1:
            delete1()
            ch2.append([r])
            f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\{}'.format(y),'ab')
            pickle.dump([r],f)
            f.close()
            rearrange()
        elif x=='done.dat' and y=='doing.dat' and [r] in ch2:
            delete2()
            ch1.append([r])
            f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\{}'.format(y),'ab')
            pickle.dump([r],f)
            f.close()
            rearrange()
        elif x=='doing.dat' and y=='todo.dat' and [r] in ch1:
            delete1()
            ch.append([r])
            f = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\{}'.format(y),'ab')
            pickle.dump([r],f)
            f.close()
            rearrange()
        lis=[]
        
        '''if y=='todo.dat':
            ch.append([r])
        elif y=='doing.dat':
            ch1.append([r])
        elif y=='done.dat':
            ch2.append([r])'''
        print("shifting complete")

labb1 = Label(can,text='                        ',font=("Arial",10))
labb1.grid(row=0,column=3)

labb3 = Label(can,text="Done",font=("Arial",15))
labb3.grid(row=0,column=4)

def doneread():
    global ch2
    ch2=[]
    f =  open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\done.dat','rb')
    try:
        while True:
            dat= pickle.load(f)
            ch2.append(dat)
            print(dat)
    except EOFError:
        f.close()
    #print(ch2)
doneread()
r2check=[]
#print(ch2)
for i in ch2:
    r3 = Radiobutton(can,text=i[0],variable=task,value=i[0],font=("Arial",10))
    r2check.append((r3,i[0]))
    r3.grid(row=ch2.index(i)+1,column=4,sticky='w')

#Notes
def opennotes():
    top = Toplevel(root)
    frame1 = Frame(top)
    frame1.pack(pady=5,padx=5)
    scroll = Scrollbar(frame1)
    scroll.pack(side=RIGHT,fill=Y)

    scroll1 = Scrollbar(frame1,orient='horizontal')
    scroll1.pack(side=BOTTOM,fill=X)

    text1 = Text(frame1,height=20,width=97,font=("Arial",12),yscrollcommand=scroll.set,xscrollcommand=scroll1.set)
    text1.pack()

    scroll1.config(command=text1.xview)

    scroll.config(command=text1.yview)

    f1 = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\text.txt','r')
    str = f1.read()
    text1.insert(1.0,str)
    lab = Label(top,text="      ")
    lab.pack(side = RIGHT)

    def save1():
        f2 = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\text.txt','w')
        f2.write(text1.get(1.0,END))
        f2.close()
        lab.config(text="Saved Successfully       ")
    f1.close()
    but11 = Button(top,text="Save",command=save1)
    but11.pack()
        

but1 = Button(can,text="Add Task",command=add,font=("Arial",10),height=2,width=10)
but1.grid(row=30,column=0)
#but2 = Button(can,text="Delete",command= delete)
#but2.grid(row=31,column=0)
but2 = Button(can,text='Update',command=update,font=("Arial",10))
but2.grid(row=31,column=0)
but3 = Button(can,text="-->",command= lambda: shift('todo.dat','doing.dat'),font=("Consolas",10),height=2,width=7)
but3.grid(row=32,column=0)
but4 = Button(can,text='<--',command= lambda: shift('doing.dat','todo.dat'),font=("Consolas",10),height=2,width=7)
but4.grid(row=30,column=2)
but5 = Button(can,text='-->',command= lambda: shift('doing.dat','done.dat'),font=("Consolas",10),height=2,width=7)
but5.grid(row=31,column=2)
but6= Button(can,text='<--',command= lambda: shift('done.dat','doing.dat'),font=("Consolas",10),height=2,width=7)
but6.grid(row=30,column=4)
#but7= Button(can,text='delete',command=delete1)
#but7.grid(row=32,column=2)
but8 = Button(can,text='Delete',command=delete2,font=("Arial",10))
but8.grid(row=31,column=4)
but10 = Button(root,text="Notes",font=("Arial",12),height=2,width=10,command=opennotes)
but10.pack()
but9 = Button(root,text="Exit",font=("Arial",12),height=2,width=10,command=root.destroy)
but9.pack()
root.mainloop()
