import pickle
import datetime
'''f1 = open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\done.dat','ab')
pickle.dump(['I am studying Maths'],f1)
print("ok done")'''
'''ch1=[]
f =  open('C:\\Users\\Atharva Goliwar\\Desktop\\My Python Projects\\doing.dat','rb')
try:
        while True:
            dat= pickle.load(f)
            ch1.append(dat)
            print(dat)
except EOFError:
        f.close()
print(ch)'''

from tkinter import *
root = Tk()
root.title("Testing the text editor")

def a1():
        print("Hello World")
def a2():
        print("Atharva is a great coder")
def a3():
        print("gg")

lis = [a1(),a2(),a3()]
lis1=[]
import random
for i in range(3):        
        x = random.randint(0,2)
        lis1.append(lis[x])
print(lis1)
for i in lis1:
        i

root.mainloop()

