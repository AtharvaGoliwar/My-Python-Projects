#Timer
from tkinter import *
import playsound
root= Tk()
class timer():
    def __init__(self):
        self.enter_time()
        root.mainloop()
    def time(self):
        self.lab = Label(root,text=self.e1.get(),font=("Arial",15))
        self.lab.pack()
        self.but = Button(root,text="Start",font=("Arial",12))
        self.but.pack()
        self.time_kame()

    def time_kame(self):
        if int(self.lab["text"]) > 0:
            self.lab["text"] = int(self.lab["text"]) - 1
            root.after(1000,self.time_kame)
        
        if int(self.lab["text"]) == 0:
            playsound.playsound('C:\\Users\\Atharva Goliwar\\Music\\Video Projects\\AUD-20201015-WA0001.mp3')
    
    def enter_time(self):
        self.e1 = Entry(root,width=10)
        self.e1.pack()
        but = Button(root,text="start",command=self.time)
        but.pack()
            
            

timer()