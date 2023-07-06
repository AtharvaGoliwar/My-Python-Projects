#Mastermind using class
from os import stat
from tkinter import *
import random
from tkinter import messagebox

root = Tk()
class game():
    def __init__(self):
        self.can = Canvas(root)
        self.can.grid(row=0,column=0)
        self.chance = IntVar()
        self.chance.set(10)
        self.lab = Label(self.can,text="No. of tries left: ")
        self.lab.grid(row=10,column=0)
        self.generate_num()
        self.grid()

    def generate_num(self):    
        lis1 = [1,2,3,4,5,6]
        self.x1 = random.choice(lis1)
        self.x2 = random.choice(lis1)
        self.x3 = random.choice(lis1)
        lbl1= Label(self.can,text='Number 1:')
        lbl1.grid(row=0,column=0)
        self.e1 = Entry(self.can,show='*',width=10)
        self.e1.insert(0,self.x1)
        self.e1.configure(state=DISABLED)
        self.e1.grid(row=0,column=1)
        lbl2= Label(self.can,text='Number 2:')
        lbl2.grid(row=1,column=0)
        self.e2 = Entry(self.can,show='*',width=10)
        self.e2.insert(0,self.x2)
        self.e2.grid(row=1,column=1)
        self.e2.configure(state=DISABLED)
        lbl3= Label(self.can,text='Number 3:')
        lbl3.grid(row=2,column=0)
        self.e3 = Entry(self.can,show='*',width=10)
        self.e3.insert(0,self.x3)
        self.e3.grid(row=2,column=1)
        self.e3.configure(state=DISABLED)
        lbl4= Label(self.can,text='Crack the code')
        lbl4.grid(row=4,column=0)

        self.lab = Label(self.can,text="",font=("Arial",12))     #The label where number will be guessed by user
        self.lab.grid(row=5,column=0)


    def grid(self):
        self.butt = Button(self.can,text='Button 1',padx=20,pady=5,command=lambda:self.b1(1))
        self.butt.grid(row=6,column=0)
        self.butt1 = Button(self.can,text='Button 2',padx=20,pady=5,command=lambda:self.b1(2))
        self.butt1.grid(row=6,column=1)
        self.butt2 = Button(self.can,text='Button 3',padx=20,pady=5,command=lambda:self.b1(3))
        self.butt2.grid(row=6,column=2)
        self.butt3 = Button(self.can,text='Button 4',padx=20,pady=5,command=lambda:self.b1(4))
        self.butt3.grid(row=7,column=0)
        self.butt4 = Button(self.can,text='Button 5',padx=20,pady=5,command=lambda:self.b1(5))
        self.butt4.grid(row=7,column=1)
        self.butt5 = Button(self.can,text='Button 6',padx=20,pady=5,command=lambda:self.b1(6))
        self.butt5.grid(row=7,column=2)

        self.but1 = Button(self.can,text="Answer",command=self.game_check)
        self.but1.grid(row=8,column=0)
        self.but2 = Button(self.can,text="Try Again",command=self.try_again)
        self.but2.grid(row=8,column=2)

    def b1(self,num):
        c = self.lab['text']
        self.lab["text"]=""
        self.lab["text"] = str(c) + str(num)
        if len(self.lab["text"])==3:
            self.butt.configure(state=DISABLED)
            self.butt1.configure(state=DISABLED)
            self.butt2.configure(state=DISABLED)
            self.butt3.configure(state=DISABLED)
            self.butt4.configure(state=DISABLED)
            self.butt5.configure(state=DISABLED)
    
    def game_check(self):
        self.a = str(self.e1.get())
        self.b = str(self.e2.get())
        self.c = str(self.e3.get())
        x = self.a + self.b + self.c
        if len(self.lab["text"])==3:
            lis = list(self.lab["text"])
            self.e5 = Label(self.can,text="")
            self.e5.grid(row=11,column=0,columnspan=3)

            #All Possible Ways of showing the hints
            if x==self.lab["text"]:
                messagebox.showinfo("MASTERMIND GAME","YOU HAVE CRACKED THE CODE!!")
                self.but1.configure(state=DISABLED)
                self.but2.configure(state=DISABLED)
            
            elif self.a in lis and self.b in lis and self.c in lis:
                if self.a==lis[0] and self.b==lis[1] or self.c==lis[2] and self.b==lis[1] or self.a==lis[0] and self.c==lis[2]:
                   self.e5["text"]=""
                   self.e5["text"]="You found the three numbers in which two are in correct position"
                elif self.a==lis[0] or self.b==lis[1] or self.c==lis[2]:
                    self.e5["text"]=""
                    self.e5["text"]= "You have found the three nubers in which one is in correct position"
                else:
                    self.e5["text"]=""
                    self.e5["text"]="You have found the three numbers"

            elif self.a in lis and self.b in lis:
                if self.a==lis[0] and self.b==lis[1]:
                    self.e5["text"]=""
                    self.e5["text"]="Two Numbers are in right position"
                elif self.a==lis[0] or self.b==lis[1]:
                    self.e5["text"]=""
                    self.e5["text"]="You have found two numbers in which one is in right position"
                else:
                    self.e5["text"]=""
                    self.e5["text"]="You have found 2 numbers"
            
            elif self.b in lis and self.c in lis:
                if self.b==lis[1] and self.c==lis[2]:
                    self.e5["text"]=""
                    self.e5["text"]="Two Numbers are in right position"
                elif self.b==lis[1] or self.c==lis[2]:
                    self.e5["text"]=""
                    self.e5["text"]="You have found two numbers in which one is in right position"
                else:
                    self.e5["text"]=""
                    self.e5["text"]="You have found 2 numbers"
            
            elif self.c in lis and self.a in lis:
                if self.a==lis[0] and self.c==lis[2]:
                    self.e5["text"]=""
                    self.e5["text"]="Two Numbers are in right position"
                elif self.a==lis[0] or self.c==lis[2]:
                    self.e5["text"]=""
                    self.e5["text"]="You have found two numbers in which one is in right position"
                else:
                    self.e5["text"]=""
                    self.e5["text"]="You have found 2 numbers"
            
            elif self.a in lis:
                if self.a==lis[0]:
                    self.e5["text"]=""
                    self.e5["text"]="One number is in correct position"
                else:
                    self.e5["text"]=""
                    self.e5["text"]="You have found one number"
            
            elif self.b in lis:
                if self.b==lis[1]:
                    self.e5["text"]=""
                    self.e5["text"]="One number is in correct position"
                else:
                    self.e5["text"]=""
                    self.e5["text"]="You have found one number"
            
            elif self.c in lis:
                if self.c==lis[2]:
                    self.e5["text"]=""
                    self.e5["text"]="One number is in correct position"
                else:
                    self.e5["text"]=""
                    self.e5["text"]="You have found one number"
            
            elif self.a not in lis and self.b not in lis and self.c not in lis:
                self.e5["text"]=""
                self.e5["text"]="None of the numbers are correct"

            self.reduce()
        else:
            self.lab["text"]=""
    def reduce(self):
        self.lab1 = Label(self.can,text="{}".format(self.chance.get()))
        self.lab1.grid(row=10,column=1)
        self.chance.set(self.chance.get() - 1)
        self.lab1["text"]=self.chance.get()
        if self.chance.get()==0:
            self.but1.configure(state=DISABLED)
            self.but2.configure(state=DISABLED)
            if (self.a + self.b + self.c)!=self.lab["text"]:
                messagebox.showinfo("MASTERMIND GAME","GAME OVER... THE REAL NUMBER WAS {}".format(self.a + self.b + self.c))

    def try_again(self):
        self.lab["text"]=""
        self.e5.destroy()
        self.butt.configure(state=ACTIVE)
        self.butt1.configure(state=ACTIVE)
        self.butt2.configure(state=ACTIVE)
        self.butt3.configure(state=ACTIVE)
        self.butt4.configure(state=ACTIVE)
        self.butt5.configure(state=ACTIVE)


game()
root.mainloop()
