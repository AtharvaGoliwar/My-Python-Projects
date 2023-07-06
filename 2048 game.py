from tkinter import *
class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        

        self.main = Frame(self,height=600,width=600,bg="black")
        self.main.grid()
        self.GUI()
        self.addingnum()
        self.mainloop()
        

    def GUI(self):
        self.lis=[]
        for i in range(4):
            rowl = []
            for j in range(4):
                rowfr = Frame(self.main,width=150,height=150)
                rowfr.grid(row=i,column=j,padx=5,pady=5)
                cellnum = Frame(self.main)
                cellnum.grid(row=i,column=j,padx=5,pady=5)
                l = Label(cellnum,text='').pack(anchor='center')
                data = cellnum
                rowl.append(data)
            self.lis.append(rowl)
        print(self.lis)        
        scorefr = Frame(self)
        scorefr.grid(row=0,column=4)
        Label(scorefr,text="Score").grid(row=0,column=0)
        scorenum = Label(scorefr,text="0").grid(row=0,column=1)

    def addingnum(self):
        import random    
        self.lis1=[]        
        x = random.randint(0,3)
        y= random.randint(0,3)
        print(x)
        print(self.lis[x][y])
        Label(self.lis[x][y],text="2",font={"Arial",15}).pack(anchor='center')
        self.lis1.append([self.lis[x][y],"2"])
        #self.lis.remove(self.lis[x][y])
            



Game()