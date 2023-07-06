from tkinter import *
from tracemalloc import start
from unicodedata import name
from PIL import Image,ImageTk
import pickle
import network
net = network.Network()
from _thread import *
#command=lambda x=r,y=c: self.click(x,y)
root = Tk()

class demo:
    def __init__(self):
        self.make_board()
        self.image()
        pr = 0
        while pr<5:
            print("Hello")
            pr+=1
        #start_new_thread(self.receive,())
        start_new_thread(self.receive_demo,())
        #self.receive()
        root.mainloop()
    def make_board(self):
        self.n = 0
        self.coords = []
        self.coords_dic = {}
        self.current_player = None
        for r in range(3):
            for c in range(3):
                but = Button(root,text="",height=4,width=9,command= lambda x=r,y=c: self.select(x,y))
                but.grid(row=r,column=c)
                self.coords.append((but,r,c))
        print(self.coords)
    def image(self):
        self.piece = []
        wpawn = Image.open('white_pawn.png')
        self.wpawn = ImageTk.PhotoImage(wpawn)
        for i in range(9):
            if self.coords[i][1]==2:
                self.coords[i][0].configure(image=self.wpawn,height=70,width=70) 

        for i in range(9):
            self.coords_dic[i]=self.coords[i][0]['image']
        print(self.coords_dic)

    def select(self,r,c):
        for i in range(9):                                                 # This loop is basically for checking if a square with "O" or red bg has been selected or not
            if self.coords[i][1]==r and self.coords[i][2]==c:
                print(self.coords[i][0]['image'])
                print(self.coords[i][0]['text'])
                if self.coords[i][0]["text"]=="O" or self.coords[i][0]['bg']=='red':             # This condition is a condition in which the piece can be captured or moved accordingly
                    try:
                        self.clear_marks()
                        self.move(r,c)
                        #start_new_thread(self.receive_demo,())
                        #self.receive_demo()
                        #self.receive()
                        start_new_thread(self.receive_demo,())
                    except:
                        print("Nahi hua")

                    
                    
        '''for i in range(64):    
            if self.coords[i][0]["text"]=="O" or self.coords[i][0]['bg']=='red':             #Removes all the previous "O" and red buttons which were made by previous selections
                self.coords[i][0].configure(text='',bg='#f0f0f0') '''
        self.clear_marks()
        
        for i in range(9):                                                                      #This loop is basically for showing all the possible ways a selected piece can move(or capture) on the chess board
                if self.coords[i][1]==r and self.coords[i][2]==c:                                #Checking following conditions for a particular selected button / pice
                    if self.coords[i][0]['image']=='pyimage1':             #WHITE PAWN
                        self.piece.clear()
                        self.piece.append(self.coords[i])
                        print(self.piece)                                                        # Storing a piece info to use it later

                        for j in range(9):
                            if self.coords[j][1]==r-1 and self.coords[j][2]==c and self.coords[j][0]['image']=='':      # Giving specific conditions to a piece(a pawn here) to create "O" and red buttons (possible moves)
                                self.coords[j][0].configure(text="O")
                                
                            if self.coords[j][1]==r-2 and r-2==4 and self.coords[j][2]==c and self.coords[j][0]['image']=='':
                                self.coords[j][0].configure(text="O")


                            '''for k in range(len(self.image_code)):
                                if self.image_code[k][0]=="black":
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c+1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')
                                    if self.coords[j][1]==r-1 and self.coords[j][2]==c-1 and self.coords[j][0]['image']==self.image_code[k][2]:
                                        self.coords[j][0].configure(bg='red',activebackground='red')'''

    def clear_marks(self):
        for i in range(9):
            if self.coords[i][0]['text']=="O" or self.coords[i][0]['bg']=='red':
                '''if (int(self.coords[i][1]) + int(self.coords[i][2])) % 2 !=0 :
                    self.coords[i][0].configure(text='',bg=self.initial_color,activebackground=self.initial_color)
                else:'''
                self.coords[i][0].configure(text='',bg='#f0f0f0',activebackground='#f0f0f0')
    
    def move(self,r,c): 
        self.n = self.n + 1       #This will help maintain alternate chances of white and black piece player
        #print(self.piece)
        for i in range(9):
            #self.coords[i][0].configure(state=ACTIVE)
            if self.coords[i][1]==r and self.coords[i][2]==c:                    #Placing the piece on the selected "O" or capture
                '''if (int(self.coords[i][1]) + int(self.coords[i][2])) % 2 !=0 :    
                    self.coords[i][0].configure(text='',image=self.piece[0][0]['image'],height=70,width=70,bg=self.initial_color,activebackground = self.initial_color)        #Moving the previous image on the new coordinates
                else:
                    self.coords[i][0].configure(text='',image=self.piece[0][0]['image'],height=70,width=70,bg='#f0f0f0')'''
                self.coords[i][0].configure(text='',image=self.piece[0][0]['image'],height=70,width=70,bg='#f0f0f0')
        self.piece[0][0].configure(image='',height=4,width=9)
        for i in range(9):
            self.coords_dic[i] = self.coords[i][0]['image']
        #print(self.coords_dic)
        data = pickle.dumps(self.coords_dic)
        print(pickle.loads(data))
        '''if self.n%2 !=0:
            net.send(data)
        else:
            while True:
                net.receive()
                if net.recv_data!="":
                    #self.coords_dic = net.recv_data
                    print(net.recv_data)
                    break'''
        net.send(data)
        '''if type(net.recv_data)==dict:
                print(net.recv_data)
                self.coords_dic = net.recv_data
                for i in range(9):
                    if self.coords_dic[i]=='':
                        self.coords[i][0].configure(height=4 , width=9,image = '')
                    else:
                        self.coords[i][0].configure(height=70,width=70,image=self.coords_dic[i])'''
        #print("Receiving")
        #self.receive_demo()
        #self.receive()
        #print("Received")
        #print(net.recv_dic)

    def receive(self):
        while True:
            print(net.recv_data)
            net.receive()
            print(net.recv_data)
            if type(net.recv_data)==dict:
                print(net.recv_data)
                self.coords_dic = net.recv_data
                for i in range(9):
                    if self.coords_dic[i]=='':
                        self.coords[i][0].configure(height=4 , width=9,image = '')
                    else:
                        self.coords[i][0].configure(height=70,width=70,image=self.coords_dic[i])
                break
            break
    def receive_demo(self):
        print(net.recv_data)
        net.receive()
        print(net.recv_data)
        if type(net.recv_data)==dict:
                print(net.recv_data)
                self.coords_dic = net.recv_data
                for i in range(9):
                    if self.coords_dic[i]=='':
                        self.coords[i][0].configure(height=4 , width=9,image = '')
                    else:
                        self.coords[i][0].configure(height=70,width=70,image=self.coords_dic[i])
        self.n = self.n + 1
        print("No. of Moves: ",self.n)
        start_new_thread(self.receive_demo,())





#demo()
def init_call():
    wait = Tk()
    lab = Label(wait,text="Waiting for connection with second game")
    lab.pack()
    '''if str(net.recv_data)=="Start Game":
        print("Destroying")
        wait.destroy()
        chess()'''
    while True:
        #print(str(net.recv_data))
        net.receive()
        #print(str(net.receive()))
        if str(net.recv_data)=="Start Game":
            #print(str(net.receive()))
            #if str(net.recv_data)=="Start Game":
                print("Destroying")
                wait.destroy()
                break
    demo()
    wait.mainloop()

if __name__== "__main__":
    init_call()

