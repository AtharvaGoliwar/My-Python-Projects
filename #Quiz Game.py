#Quiz Game
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root = Tk()
root.title("QUIZ")

lab = Label(root,text="QUIZ GAME",font=("Arial",15))
lab.pack()
global count
can = Canvas(root)
can.pack()
lab2 = Label(can,text="testing lets see....")
lab2.pack()
count=0
quests=["q2"]
def q1():
    global can
    can.destroy()
    can = Canvas(root)
    can.pack()
    lab1 = Label(can,text="Q1: What is the capital of India")
    lab1.pack()
    ans1 = StringVar()
    ans1.set("")
    op1 = Radiobutton(can,text="Delhi",value="Delhi",variable=ans1)
    op1.pack()
    op2 = Radiobutton(can,text="Maharashtra",value="Maharashtra",variable=ans1)
    op2.pack()
    op3 = Radiobutton(can,text="UP",value="UP",variable=ans1)
    op3.pack()
    op4 = Radiobutton(can,text="Karnataka",value="Karnataka",variable=ans1)
    op4.pack()
    def save():
        global count
        print("Saving")
        if ans1.get()=="Delhi":
            count+=1
            q2()
        else:
            q2()

                    
                    
    but2 = Button(can,text="Save and Next",command=save)
    but2.pack()
def q2():
    global can
    can.destroy()
    can=Canvas(root)
    can.pack()
    lab3 = Label(can,text="Q2: If weight of a man on earth is 600 N then what will be the mass of the man on moon?")
    lab3.pack()
    ans2 = StringVar()
    ans2.set("")
    op1 = Radiobutton(can,text="600",variable=ans2,value="600")
    op1.pack()
    op2 = Radiobutton(can,text="60",variable=ans2,value="60")
    op2.pack()
    op2 = Radiobutton(can,text="100",variable=ans2,value="100")
    op2.pack()
    op2 = Radiobutton(can,text="100",variable=ans2,value="10")
    op2.pack()
    def save1():
        global count
        if ans2.get()=="60":
            count+=1
            q3()
        else:
            q3()
    but2 = Button(can,text="Save and Next",command=save1)
    but2.pack()
def q3():
    global can
    can.destroy()
    can=Canvas(root)
    can.pack()
    lab1 = Label(can,text="Q3: Which is the programming language of future?")
    lab1.pack()
    ans3 = StringVar()
    ans3.set("")
    op1 = Radiobutton(can,text="Java",value="Java",variable=ans3)
    op1.pack()
    op2 = Radiobutton(can,text="C++",value="C++",variable=ans3)
    op2.pack()
    op3 = Radiobutton(can,text="Python",value="Python",variable=ans3)
    op3.pack()
    op4 = Radiobutton(can,text="HTML",value="HTML",variable=ans3)
    op4.pack()
    def save2():
        global count
        if ans3.get()=="Python":
            count+=1
            messagebox.showinfo("QUIZ","YOUR SCORE IS {} OUT OF 3".format(count))
        else:
            messagebox.showinfo("QUIZ","YOUR SCORE IS {} OUT OF 3".format(count))

        
    but2 = Button(can,text="Save and Submit",command=save2)
    but2.pack()
but1 = Button(can,text="can des",command=q1)
but1.pack()

root.mainloop()