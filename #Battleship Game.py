#Battleship Game
from tkinter import *
from tkinter import messagebox
import random
import mysql.connector
mycon = mysql.connector.connect(host='localhost',username='root',passwd='abc123',database='battlefield')
c = mycon.cursor()

root = Tk()

class game():
	def __init__(self):
		self.grid()
		self.computer_selection()
		root.mainloop()

	def grid(self):
		self.coords_AI = []
		self.comp_played_coords = []
		self.win_user = 0
		self.win_comp = 0
		self.coords = []
		self.coords1 = []
		for r in range(10):
			for c in range(10):
				but1 = Button(root,text='',height=2,width=5,command= lambda x=r,y=c: self.click(x,y))
				but1.grid(row=r,column=c)
				self.coords.append((but1,r,c))

		lab = Label(root,text="                               ")
		lab.grid(row=0,column=11)

		for r in range(10):
			for c in range(10):
				but1 = Button(root,text='',height=2,width=5,command= lambda x=r,y=c+12: self.player_choose(x,y),state=DISABLED)
				but1.grid(row=r,column=c+12)
				self.coords1.append((but1,r,c+12))

		self.ship_name = StringVar()
		self.ship_name.set("")
		print(self.ship_name.get())

		opt1 = Radiobutton(root,text="Carrier",variable = self.ship_name,value='Carrier')
		opt1.grid(row=12,column=0,columnspan=2)
		opt2 = Radiobutton(root,text="Boat",variable=self.ship_name,value="Boat")
		opt2.grid(row=12,column=2,columnspan=2)
		opt3 = Radiobutton(root,text='Submarine',variable=self.ship_name,value='Submarine')
		opt3.grid(row=12,column=4,columnspan=2)
		opt4 = Radiobutton(root,text='Ship',variable=self.ship_name,value='Ship')
		opt4.grid(row=12,column=6,columnspan=2)
		self.carr_n = 0
		self.carr_check_coords = []
		self.boat_n = 0
		self.boat_check_coords = []
		self.subm_n = 0
		self.subm_check_coords = []
		self.ship_n = 0
		self.ship_check_coords = []

		but_clear = Button(root,text="Clear",command= self.clear_grid)
		but_clear.grid(row=13,column=0)
		but_start = Button(root,text="Start",command= self.start)
		but_start.grid(row=14,column=0)


	def click(self,r,c):
		if self.ship_name.get()=='Carrier' and self.carr_n<4:
			for i in range(100):
				if self.coords[i][1]==r and self.coords[i][2]==c:
					self.carr_check_coords.append(self.coords[i])
					self.coords[i][0].configure(bg='green',activebackground='green')
					self.carr_n = self.carr_n + 1
					print('hello world')
					print(self.coords[i][0]['bg'])
		if self.carr_n==4:
			print(self.carr_check_coords)
			for i in range(100):
				if len(self.carr_check_coords) != 0:
					if self.coords[i][1]==self.carr_check_coords[0][1] and self.coords[i][2]==self.carr_check_coords[0][2]:
						print(type(self.coords[i][0]['bg']))
						if i>2 and self.coords[i][0]['bg']==self.coords[i-1][0]['bg']==self.coords[i-2][0]['bg']==self.coords[i-3][0]['bg']=='green':
							print("all ok")
						elif i<98 and self.coords[i][0]['bg']==self.coords[i+1][0]['bg']==self.coords[i+2][0]['bg']==self.coords[i+3][0]['bg']=='green':
							print("all ok")
						elif i<71 and self.coords[i][0]['bg']==self.coords[i+10][0]['bg']==self.coords[i+20][0]['bg']==self.coords[i+30][0]['bg']=='green':
							print("all ok")
						elif i>29 and self.coords[i][0]['bg']==self.coords[i-10][0]['bg']==self.coords[i-20][0]['bg']==self.coords[i-30][0]['bg']=='green':
							print("all ok")
						else:
							for k in range(4):
								self.carr_check_coords[k][0].configure(bg="#f0f0f0",activebackground='#f0f0f0')
							self.carr_check_coords.clear()
							self.carr_n=0

		if self.ship_name.get()=="Boat" and self.boat_n<2:
			for i in range(100):
				if self.coords[i][1]==r and self.coords[i][2]==c:
					self.boat_check_coords.append(self.coords[i])
					self.coords[i][0].configure(bg='orange',activebackground='orange')
					self.boat_n = self.boat_n + 1
		if self.boat_n==2:
			for i in range(100):
				if len(self.boat_check_coords) != 0:
					if self.coords[i][1]==self.boat_check_coords[0][1] and self.coords[i][2]==self.boat_check_coords[0][2]:
						print(type(self.coords[i][0]['bg']))
						if i>0 and self.coords[i][0]['bg']==self.coords[i-1][0]['bg']=='orange':
							print("all ok")
						elif i<99 and self.coords[i][0]['bg']==self.coords[i+1][0]['bg']=='orange':
							print("all ok")
						elif i<90 and self.coords[i][0]['bg']==self.coords[i+10][0]['bg']=='orange':
							print("all ok")
						elif i>9 and self.coords[i][0]['bg']==self.coords[i-10][0]['bg']=='orange':
							print("all ok")
						else:
							for k in range(2):
								self.boat_check_coords[k][0].configure(bg="#f0f0f0",activebackground='#f0f0f0')
							self.boat_check_coords.clear()
							self.boat_n=0

		if self.ship_name.get()=='Submarine' and self.subm_n < 3:
			for i in range(100):
				if self.coords[i][1]==r and self.coords[i][2]==c:
					self.subm_check_coords.append(self.coords[i])
					self.coords[i][0].configure(bg='purple',activebackground='purple')
					self.subm_n = self.subm_n + 1
		if self.subm_n==3:
			print(self.subm_check_coords)
			for i in range(100):
				if len(self.subm_check_coords) != 0:
					if self.coords[i][1]==self.subm_check_coords[0][1] and self.coords[i][2]==self.subm_check_coords[0][2]:
						print(type(self.coords[i][0]['bg']))
						if i>1 and self.coords[i][0]['bg']==self.coords[i-1][0]['bg']==self.coords[i-2][0]['bg']=='purple':
							print("all ok")
						elif i<99 and self.coords[i][0]['bg']==self.coords[i+1][0]['bg']==self.coords[i+2][0]['bg']=='purple':
							print("all ok")
						elif i<81 and self.coords[i][0]['bg']==self.coords[i+10][0]['bg']==self.coords[i+20][0]['bg']=='purple':
							print("all ok")
						elif i>19 and self.coords[i][0]['bg']==self.coords[i-10][0]['bg']==self.coords[i-20][0]['bg']=='purple':
							print("all ok")
						else:
							for k in range(3):
								self.subm_check_coords[k][0].configure(bg="#f0f0f0",activebackground='#f0f0f0')
							self.subm_check_coords.clear()
							self.subm_n=0

		if self.ship_name.get()=='Ship' and self.ship_n < 3:
			for i in range(100):
				if self.coords[i][1]==r and self.coords[i][2]==c:
					self.ship_check_coords.append(self.coords[i])
					self.coords[i][0].configure(bg='lime green',activebackground='lime green')
					self.ship_n = self.ship_n + 1
		if self.ship_n==3:
			print(self.ship_check_coords)
			for i in range(100):
				if len(self.ship_check_coords) != 0:
					if self.coords[i][1]==self.ship_check_coords[0][1] and self.coords[i][2]==self.ship_check_coords[0][2]:
						print(type(self.coords[i][0]['bg']))
						if i>1 and self.coords[i][0]['bg']==self.coords[i-1][0]['bg']==self.coords[i-2][0]['bg']=='lime green':
							print("all ok")
						elif i<99 and self.coords[i][0]['bg']==self.coords[i+1][0]['bg']==self.coords[i+2][0]['bg']=='lime green':
							print("all ok")
						elif i<81 and self.coords[i][0]['bg']==self.coords[i+10][0]['bg']==self.coords[i+20][0]['bg']=='lime green':
							print("all ok")
						elif i>19 and self.coords[i][0]['bg']==self.coords[i-10][0]['bg']==self.coords[i-20][0]['bg']=='lime green':
							print("all ok")
						else:
							for k in range(3):
								self.ship_check_coords[k][0].configure(bg="#f0f0f0",activebackground='#f0f0f0')
							self.ship_check_coords.clear()
							self.ship_n=0

	def clear_grid(self):
		for i in range(100):
			self.coords[i][0].configure(bg='#f0f0f0',activebackground='#f0f0f0')
		self.carr_check_coords.clear()
		self.carr_n = 0
		self.ship_check_coords.clear()
		self.ship_n = 0
		self.subm_check_coords.clear()
		self.subm_n = 0
		self.boat_check_coords.clear()
		self.boat_n = 0

	def start(self):
		self.game_turns = 0
		if len(self.carr_check_coords)==4 and len(self.boat_check_coords)==2 and len(self.subm_check_coords)==3 and len(self.ship_check_coords)==3:
			for i in range(100):
				self.coords[i][0].configure(state=DISABLED)
				self.coords1[i][0].configure(state=ACTIVE)
			carr_loc = []
			ship_loc = []
			boat_loc = []
			subm_loc = []

			carr_loc_final = ''
			ship_loc_final = ''
			boat_loc_final = ''
			subm_loc_final = ''
			for j in range(4):
				carr_loc.append((self.carr_check_coords[j][1],self.carr_check_coords[j][2]))
			for j in range(3):
				ship_loc.append((self.ship_check_coords[j][1],self.ship_check_coords[j][2]))
			for j in range(2):
				boat_loc.append((self.boat_check_coords[j][1],self.boat_check_coords[j][2]))
			for j in range(3):
				subm_loc.append((self.subm_check_coords[j][1],self.subm_check_coords[j][2]))

			for i in range(len(str(carr_loc))):
				if str(carr_loc)[i]=='[' or str(carr_loc)[i]==']' or str(carr_loc)[i]==' ' or str(carr_loc)[i]==',' or str(carr_loc)[i]==')' or str(carr_loc)[i]=='(':
					continue
				else:      
					carr_loc_final = carr_loc_final + str(carr_loc)[i]
			print(carr_loc_final)
			for i in range(len(str(ship_loc))):
				if str(ship_loc)[i]=='[' or str(ship_loc)[i]==']' or str(ship_loc)[i]==' ' or str(ship_loc)[i]==',' or str(ship_loc)[i]==')' or str(ship_loc)[i]=='(':
					continue
				else:      
					ship_loc_final = ship_loc_final + str(ship_loc)[i]
			print(ship_loc_final)
			for i in range(len(str(boat_loc))):
				if str(boat_loc)[i]=='[' or str(boat_loc)[i]==']' or str(boat_loc)[i]==' ' or str(boat_loc)[i]==',' or str(boat_loc)[i]==')' or str(boat_loc)[i]=='(':
					continue
				else:      
					boat_loc_final = boat_loc_final + str(boat_loc)[i]
			print(boat_loc_final)
			for i in range(len(str(subm_loc))):
				if str(subm_loc)[i]=='[' or str(subm_loc)[i]==']' or str(subm_loc)[i]==' ' or str(subm_loc)[i]==',' or str(subm_loc)[i]==')' or str(subm_loc)[i]=='(':
					continue
				else:      
					subm_loc_final = subm_loc_final + str(subm_loc)[i]
			print(subm_loc_final)

			q1 = "insert into locations values('{}','{}','{}','{}')".format(carr_loc_final,ship_loc_final,boat_loc_final,subm_loc_final)
			c.execute(q1)
			mycon.commit()

		else:
			messagebox.showerror("Battleship Game","Send all your troops on the battlefield")

	def computer_selection(self):
		q1 = 'select * from locations'
		c.execute(q1)
		dat1 = c.fetchall()
		pat = random.randint(0,len(dat1))
		print(dat1[pat])
		self.comp_carr_coords = []
		self.comp_ship_coords = []
		self.comp_boat_coords = []
		self.comp_subm_coords = []
		if len(dat1[pat][0])==8:
			for i in range(0,8,2):
				self.comp_carr_coords.append((int(dat1[pat][0][i]),int(dat1[pat][0][i+1])))
		print(self.comp_carr_coords)

		if len(dat1[pat][1])==6:
			for i in range(0,6,2):
				self.comp_ship_coords.append((int(dat1[pat][1][i]),int(dat1[pat][1][i+1])))
		print(self.comp_ship_coords)

		if len(dat1[pat][2])==4:
			for i in range(0,4,2):
				self.comp_boat_coords.append((int(dat1[pat][2][i]),int(dat1[pat][2][i+1])))

		if len(dat1[pat][3])==6:
			for i in range(0,6,2):
				self.comp_subm_coords.append((int(dat1[pat][3][i]),int(dat1[pat][3][i+1])))
		print(self.comp_subm_coords)

	def player_choose(self,r,c):
		for i in range(100):
			if self.coords1[i][1]==r and self.coords1[i][2]==c:
				if (self.coords1[i][1],self.coords1[i][2]-12) in self.comp_carr_coords or (self.coords1[i][1],self.coords1[i][2]-12) in self.comp_ship_coords or (self.coords1[i][1],self.coords1[i][2]-12) in self.comp_boat_coords or (self.coords1[i][1],self.coords1[i][2]-12) in self.comp_subm_coords :
					self.coords1[i][0].configure(bg='red',activebackground='red',state=DISABLED)
					self.win_user = self.win_user + 1
					self.game_turns = self.game_turns + 1
				else:
					self.coords1[i][0].configure(bg='blue',activebackground='blue',state=DISABLED)
					self.game_turns = self.game_turns + 1

		self.comp_play()

		if self.win_user == 12:
			messagebox.showinfo("Battleship","Ypu won")

	def comp_play(self):
		## FOR AI , ALREADY A LIST IS CREATED , FROM THAT LIST NOW CHECK IN ALL POSSIBLE DIRECTIONS FOR ANOTHER HIT, IF YES THEN CONTINUE SAME PROCESS ELSE CLEAR THE LIST AND START RANDOM HITS AGAIN
		n = 1
		while n==1:
			x = random.randint(0,9)
			y = random.randint(0,9)
			if (x,y) not in self.comp_played_coords:
				self.comp_played_coords.append((x,y))
				n = 0
			else:
				n = 1
		print(x,y)
		only_user_carr_coords = []
		only_user_ship_coords = []
		only_user_boat_coords = []
		only_user_subm_coords = []
		for i in range(4):
			only_user_carr_coords.append((self.carr_check_coords[i][1],self.carr_check_coords[i][2]))
		for i in range(3):
			only_user_ship_coords.append((self.ship_check_coords[i][1],self.ship_check_coords[i][2]))
		for i in range(2):
			only_user_boat_coords.append((self.boat_check_coords[i][1],self.boat_check_coords[i][2]))
		for i in range(3):
			only_user_subm_coords.append((self.subm_check_coords[i][1],self.subm_check_coords[i][2]))

		for i in range(100):
			if self.coords[i][1]==x and self.coords[i][2]==y:
				if (self.coords[i][1],self.coords[i][2]) in only_user_carr_coords or (self.coords[i][1],self.coords[i][2]) in only_user_ship_coords or (self.coords[i][1],self.coords[i][2]) in only_user_boat_coords or (self.coords[i][1],self.coords[i][2]) in only_user_subm_coords:
					self.coords[i][0].configure(bg='red',activebackground='red',state=DISABLED)
					self.win_comp = self.win_comp + 1
					self.coords_AI.append((x,y))
				else:
					self.coords[i][0].configure(bg='blue',activebackground='blue',state=DISABLED)
		if self.win_comp==12:
			messagebox.showinfo("Battleship","comp won")
					
game()

## Basic plan what to make:
	# 10x10 grid game (at first make 1 player game only)
	# 4 ships each player. Every ships health will be visible at one side of the game
	# For testing start with green grids as ships.... later edit a few images
	