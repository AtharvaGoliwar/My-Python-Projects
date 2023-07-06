#The Snake Game
from tkinter import *
from PIL import Image,ImageTk

root = Tk()

class snake_game():
	def __init__(self):
		self.grid()
		#root.after(1000,self.move)
		root.bind("d",lambda event: self.change_dir(event,'right'))
		root.bind("s",lambda event: self.change_dir(event,'down'))
		root.bind("a",lambda event: self.change_dir(event,'left'))

		root.mainloop()

	def grid(self):
		self.dir = 'right'
		self.head = 82
		self.snake_len = 3
		self.coords = []
		self.snake_curr_coords = []
		#score_label = Label(root,text="Score: ")
		#score_label.grid(row=0,column=30)

		snake = Image.open('C://Users//Atharva//OneDrive//Desktop//My Python Projects//Snake Game//snake.png')
		snake_img = ImageTk.PhotoImage(snake)

		for r in range(25):
			for c in range(25):
				frame = Frame(root,height=20,width=20,bg='black')
				frame.grid(row=r,column=c)
				self.coords.append((frame,r,c))

		print(self.coords)

		self.coords[80][0].configure(bg='green')
		self.coords[81][0].configure(bg='green')
		self.coords[82][0].configure(bg='green')

		self.snake_curr_coords.append(self.coords[80])
		self.snake_curr_coords.append(self.coords[81])
		self.snake_curr_coords.append(self.coords[82])

		self.move()

		
	def move(self):
		if self.dir=='right':
			if (self.head+1)%25!=0:
				self.coords[self.head + 1][0].configure(bg='green')
				self.coords[(self.head + 1) - self.snake_len][0].configure(bg='black')
				self.head+=1
				root.after(1000,self.move)
			else:
				print("out")

		elif self.dir=='down':
			self.coords[self.head + 25][0].configure(bg='green')
			self.coords[(self.head + 25) - 75][0].configure(bg='black')
			self.head+=25
			root.after(1000,self.move)

		elif self.dir=='left':
			self.coords[self.head - 1][0].configure(bg='green')
			self.coords[(self.head-1) + self.snake_len][0].configure(bg='black')
			self.head-=1
			root.after(1000,self.move)

	def change_dir(self,event,direct):
		if direct=='right':
			self.dir = 'right'
			self.move()
		elif direct=='down':
			self.dir='down'
			self.move
		elif direct=='left':
			self.dir='left'
			self.move

		


snake_game()