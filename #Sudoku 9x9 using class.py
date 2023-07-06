#Sudoku 9x9 using class
from tkinter import *
from tkinter import messagebox

class sudoku():
    def __init__(self):
        self.root = Tk()
        self.grid()
        self.root.title("SUDOKU 9X9")
        self.root.mainloop()

    def grid(self):
        self.boxlis = []                    ## The list where all the buttons will be stored which are organised row wise
        self.num = StringVar()
        self.num.set("")
        for r in range(9):
            tup=[]
            for c in range(9):
                print(r,c)
                but = Button(self.root,text="",font=("Arial",12),bg="ghost white",activebackground="ghost white",height=2,width=5, command = lambda x=r,y=c: self.click(x,y))
                but.grid(row=r,column=c)
                tup.append((but,r,c))
            self.boxlis.append(tup)
        for i in range(9):
            rad = Radiobutton(self.root,text=i+1,value=i+1,variable=self.num,font=("Arial",12))
            rad.grid(row=9,column=i)

        self.checkbox()                            ##Had to call checkbox so that can access the box lists
        self.colorbox()

        ##The puzzle
        self.dis(0,0,"7")
        self.dis(0,1,"2")
        self.dis(0,2,"3")
        self.dis(0,6,"1")
        self.dis(0,7,"5")
        self.dis(0,8,"9")

        self.dis(1,0,"6")
        self.dis(1,3,"3")
        self.dis(1,5,"2")
        self.dis(1,8,"8")

        self.dis(2,0,"8")
        self.dis(2,4,"1")
        self.dis(2,8,"2")

        self.dis(3,1,"7")
        self.dis(3,3,"6")
        self.dis(3,4,'5')
        self.dis(3,5,'4')
        self.dis(3,7,'2')

        self.dis(4,2,'4')
        self.dis(4,3,'2')
        self.dis(4,5,'7')
        self.dis(4,6,'3')

        self.dis(5,1,'5')
        self.dis(5,3,'9')
        self.dis(5,4,'3')
        self.dis(5,5,'1')
        self.dis(5,7,'4')

        self.dis(6,0,'5')
        self.dis(6,4,'7')
        self.dis(6,8,'3')

        self.dis(7,0,'4')
        self.dis(7,3,'1')
        self.dis(7,5,'3')
        self.dis(7,8,'6')

        self.dis(8,0,'9')
        self.dis(8,1,'3')
        self.dis(8,2,'2')
        self.dis(8,6,'7')
        self.dis(8,7,'1')
        self.dis(8,8,'4')

    def click(self,a,b):
        self.boxlis[a][b][0]["text"] = self.num.get()
        self.checkrow()
        self.checkcolumn()
        self.checkbox()
        if len(self.winrow)==9:
            print("HURRAYYY!!!!")
        if len(self.wincolumn)==9:
            print("ARARARAR KHATARNAK")
        if len(self.winbox)==9:
            print("Well done bete!!!")
        if len(self.winrow)==9 and len(self.wincolumn)==9 and len(self.winbox)==9:
            messagebox.showinfo("Sudoku","YOU CRACKED THE GAME")
        
    #For all the checks , in general we will follow this:
    #1. Get all the required buttons in a list of tuples where in each tuple there will be the buttons
    #2. Check if all 9 buttons have different numbers
    #3. If yes then append a W
    def checkrow(self):
        row = []                       #The list which has 9 lists (named tup) which are arranged row wise
        self.winrow = []
        for r in range(9):
            tup=[]
            for c in range(9):
                tup.append(self.boxlis[r][c][0])
            row.append(tup)
        
        for rowtuple in row:
            n = []                           ##List n which has unique digits from 1 to 9
            for i in range(9):
                if rowtuple[i]["text"] not in n and rowtuple[i]["text"]!= "":             ##The check condition to make every element in n unique
                    n.append(rowtuple[i]["text"])
            if len(n)==9:
                self.winrow.append("W")        ##If the row (the list tup) has all numbers unique then append a W in win list

    def checkcolumn(self):                     ## (Done similar to above check function)
        column=[]
        self.wincolumn = []
        for c in range(9):
            tup=[]
            for r in range(9):
                tup.append(self.boxlis[r][c][0])
            column.append(tup)
        
        for columntuple in column:
            n=[]
            for i in range(9):
                if columntuple[i]["text"] not in n and columntuple[i]["text"] != "":
                    n.append(columntuple[i]["text"])
            
            if len(n)==9:
                self.wincolumn.append("W")

    def checkbox(self):
        self.box = []
        self.winbox=[]
        for r in range(0,9,3):
            tup=[]                    ## The list which has lists of 3 boxes of a particular row  (a box row has 3 columns n 3 rows)
            for c in range(0,9,3):
                tup.append([self.boxlis[r][c][0],self.boxlis[r][c+1][0],self.boxlis[r][c+2][0],self.boxlis[r+1][c][0],self.boxlis[r+1][c+1][0],self.boxlis[r+1][c+2][0],self.boxlis[r+2][c][0],self.boxlis[r+2][c+1][0],self.boxlis[r+2][c+2][0]])
                print(tup)
            self.box.append(tup)
        print(self.box)
        print(len(self.box))
        
        for boxtuple in self.box:              ## Boxtuple is the list which has 3 boslists in it which have to be itterated
            print(boxtuple)
            for i in range(3):
                n=[]
                for j in range(9):
                        if boxtuple[i][j]["text"] not in n and boxtuple[i][j]["text"]!="":
                            n.append(boxtuple[i][j]["text"])
                print(n)
                if len(n)==9:
                    self.winbox.append("W")

    def colorbox(self):
        boxcolor = [self.box[0][0],self.box[0][2],self.box[1][1],self.box[2][0],self.box[2][2]]
        for box in boxcolor:
            for i in range(9):
                box[i].configure(bg="gainsboro",activebackground="gainsboro")

    def dis(self,r,c,t):
        self.boxlis[r][c][0].configure(text=t,state=DISABLED)
                
sudoku()
                
