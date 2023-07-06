#Tic Tac Toe using class
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tic Tac Toe")
s1 = 0
s2 = 0
class game():
    def __init__(self):
        self.n = 0
        self.op = StringVar()
        self.op.set("")
        self.grid()

    def grid(self):
        self.but = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but),font=("Arial",15))
        self.but.grid(row=0,column=0,sticky='n')
        self.but1 = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but1),font=("Arial",15))
        self.but1.grid(row=0,column=1,sticky='n')
        self.but2 = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but2),font=("Arial",15))
        self.but2.grid(row=0,column=2,sticky='n')

        self.but3 = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but3),font=("Arial",15))
        self.but3.grid(row=1,column=0,sticky='n')
        self.but4 = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but4),font=("Arial",15))
        self.but4.grid(row=1,column=1,sticky='n')
        self.but5 = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but5),font=("Arial",15))
        self.but5.grid(row=1,column=2,sticky='n')

        self.but6 = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but6),font=("Arial",15))
        self.but6.grid(row=2,column=0,sticky='n')
        self.but7 = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but7),font=("Arial",15))
        self.but7.grid(row=2,column=1,sticky='n')
        self.but8 = Button(root,text=self.op.get(),height=2,width=5,command=lambda: self.click(self.but8),font=("Arial",15))
        self.but8.grid(row=2,column=2,sticky='n')

    def click(self,b):
        if self.n==0 or self.n==2 or self.n==4 or self.n==6 or self.n==8:
            if b["text"]=="":
                self.op.set("X")
                b["text"]="X"
                self.n+=1
        elif self.n==1 or self.n==3 or self.n==5 or self.n==7 or self.n==9:
            if b["text"]=="":
                self.op.set("O")
                b["text"]="O"
                self.n+=1
        
        self.check()

    def check(self):
        if self.but["text"]==self.but4["text"]==self.but8["text"]=="X" or self.but["text"]==self.but4["text"]==self.but8["text"]=="O":
            response = messagebox.showinfo("Tic Tac Toe","The winner of this game is '{}' user".format(self.op.get()))
            print(response)
            self.dis()
            self.scores()
        elif self.but2["text"]==self.but4["text"]==self.but6["text"]=="X" or self.but2["text"]==self.but4["text"]==self.but6["text"]=="O":
            response = messagebox.showinfo("Tic Tac Toe","The winner of this game is '{}' user".format(self.op.get()))
            print(response)
            self.dis()
            self.scores()

        elif self.but["text"]==self.but1["text"]==self.but2["text"]=="X" or self.but["text"]==self.but1["text"]==self.but2["text"]=="O":
            response = messagebox.showinfo("Tic Tac Toe","The winner of this game is '{}' user".format(self.op.get()))
            print(response)
            self.dis()
            self.scores()
        elif self.but3["text"]==self.but4["text"]==self.but5["text"]=="X" or self.but3["text"]==self.but4["text"]==self.but5["text"]=="O" :
            response = messagebox.showinfo("Tic Tac Toe","The winner of this game is '{}' user".format(self.op.get()))
            print(response)
            self.dis()
            self.scores()
        elif self.but6["text"]==self.but7["text"]==self.but8["text"]=="X" or self.but6["text"]==self.but7["text"]==self.but8["text"]=="O" :
            response = messagebox.showinfo("Tic Tac Toe","The winner of this game is '{}' user".format(self.op.get()))
            print(response)
            self.dis()
            self.scores()
        elif self.but["text"]==self.but3["text"]==self.but6["text"]=="X" or self.but["text"]==self.but3["text"]==self.but6["text"]=="O":
            response = messagebox.showinfo("Tic Tac Toe","The winner of this game is '{}' user".format(self.op.get()))
            print(response)
            self.dis()
            self.scores()
        elif self.but1["text"]==self.but4["text"]==self.but7["text"]=="X" or self.but1["text"]==self.but4["text"]==self.but7["text"]=="O":
            response = messagebox.showinfo("Tic Tac Toe","The winner of this game is '{}' user".format(self.op.get()))
            print(response)
            self.dis()
            self.scores()
        elif self.but2["text"]==self.but5["text"]==self.but8["text"]=="X" or self.but2["text"]==self.but5["text"]==self.but8["text"]=="O" :
            response = messagebox.showinfo("Tic Tac Toe","The winner of this game is '{}' user".format(self.op.get()))
            print(response)
            self.dis()
            self.scores()
        elif self.n==9:
            response = messagebox.showinfo("Tic Tac Toe","The Game has been Tied")
            print(response)
            self.dis()
    
    def scores(self):
        if self.op.get()=="X":
            global s1
            s1+=1
        elif self.op.get()=="O":
            global s2
            s2+=1
        labe1 = Label(root,text="Score of X: {}".format(s1))
        labe1.grid(row=0,column=5)
        labe2 = Label(root,text="Score of O: {}".format(s2))
        labe2.grid(row=1,column=5)
    
    def dis(self):
        self.but.configure(state=DISABLED)
        self.but1.configure(state=DISABLED)
        self.but2.configure(state=DISABLED)
        self.but3.configure(state=DISABLED)
        self.but4.configure(state=DISABLED)
        self.but5.configure(state=DISABLED)
        self.but6.configure(state=DISABLED)
        self.but7.configure(state=DISABLED)
        self.but8.configure(state=DISABLED)  
            

game()
labe1 = Label(root,text="Score of X: 0")
labe1.grid(row=0,column=5)
labe2 = Label(root,text="Score of O: 0")
labe2.grid(row=1,column=5)
labe = Label(root,text='       ')
labe.grid(row=0,column=4)
butt1 = Button(root,text="Play again",padx=20,pady=20,command=game)
butt1.grid(row=2,column=5)

root.mainloop()