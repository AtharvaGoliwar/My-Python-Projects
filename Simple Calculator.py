from tkinter import *
import math
root=Tk()
root.title("SIMPLE CALCULATOR")

e= Entry(root, width=50)
e.grid(row=0,column=0,columnspan = 3, padx=10,pady=10)
def button_click(number):
        c = e.get()
        e.delete(0,END)
        e.insert(0, str(c)+str(number))
        return
def button_click1():
        a= e.get()
        e.delete(0,END)
        e.insert(0,str(a)+'.')
def button_clear():
        e.delete(0, END)
def button_add():
        first_number = e.get()
        global f_num
        global maths
        maths='add'
        f_num = float(first_number)
        e.delete(0,END)
def button_equal():
        sec_num = e.get()
        e.delete(0,END)
        if maths=='add':
                e.insert(0, float(sec_num) + f_num)
        elif maths=='Subtraction':
                e.insert(0, f_num - float(sec_num))
        elif maths=='Multi':
                e.insert(0, f_num * float(sec_num))
        elif maths=='Divide':
                e.insert(0, f_num / float(sec_num))
        elif maths=='power':
                e.insert(0, math.pow(f_num,float(sec_num)))
        elif maths=='sqrt':
                e.insert(0, math.sqrt(f_num))
def button_sub():
        first_number = e.get()
        global f_num
        global maths
        maths='Subtraction'
        f_num = float(first_number)
        e.delete(0,END)
def button_mult():
       first_number = e.get()
       global f_num
       global maths
       maths='Multi'
       f_num = float(first_number)
       e.delete(0,END)
def button_div():
        first_number = e.get()
        global f_num
        global maths
        maths='Divide'
        f_num = float(first_number)
        e.delete(0,END)
def button_pow():
        first_number = e.get()
        global f_num
        global maths
        maths='power'
        f_num = float(first_number)
        e.delete(0,END)
def button_sqrt():
        first_number = e.get()
        global f_num
        global maths
        maths='sqrt'
        f_num = float(first_number)
        e.delete(0,END)


#define button

button_1 = Button(root, text = '1' , padx = 40, pady = 20, command=lambda: button_click(1))
button_2 = Button(root, text = '2' , padx = 40, pady = 20, command=lambda: button_click(2))
button_3 = Button(root, text = '3' , padx = 40, pady = 20, command=lambda: button_click(3))
button_4 = Button(root, text = '4' , padx = 40, pady = 20, command=lambda: button_click(4))
button_5 = Button(root, text = '5' , padx = 40, pady = 20, command=lambda: button_click(5))
button_6 = Button(root, text = '6' , padx = 40, pady = 20, command=lambda: button_click(6))
button_7 = Button(root, text = '7' , padx = 40, pady = 20, command=lambda: button_click(7))
button_8 = Button(root, text = '8' , padx = 40, pady = 20, command=lambda: button_click(8))
button_9 = Button(root, text = '9' , padx = 40, pady = 20, command=lambda: button_click(9))
button_0 = Button(root, text = '0' , padx = 40, pady = 20, command=lambda: button_click(0))
butt_add = Button(root, text = '+' , padx = 40, pady = 20, command=button_add)
butt_equal = Button(root, text = '=' , padx = 90, pady = 20, command=button_equal)
butt_clear = Button(root, text = 'Clear' , padx = 80, pady = 20, command=button_clear)
butt_sub= Button(root, text='-' , padx = 40, pady=20, command= button_sub)
butt_mult= Button(root, text='x' , padx = 40, pady=20, command= button_mult)
butt_div= Button(root, text='/' , padx = 40, pady=20, command= button_div)
butt_pow= Button(root, text='^' , padx = 40, pady=20, command= button_pow)
butt_sqrt= Button(root, text='rt' , padx = 40, pady=20, command= button_sqrt)
butt_poi= Button(root,text='.',padx=40,pady=20,command=button_click1)



#put buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

butt_clear.grid(row=5,column=1,columnspan=2)
butt_add.grid(row=5,column=0)
butt_sub.grid(row=6,column=0)
butt_equal.grid(row=4,column=1,columnspan=2)
butt_mult.grid(row=6,column=1)
butt_div.grid(row=6,column=2)
butt_pow.grid(row=1,column=3)
butt_sqrt.grid(row=2,column=3)
butt_poi.grid(row=3,column=3)

root.mainloop()
