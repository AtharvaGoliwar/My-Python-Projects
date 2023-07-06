import tkinter as tk
from random import randint
from PIL import Image, ImageTk
#import mysql.connector
#mycon = mysql.connector.connect(host='localhost',user='root',passwd=
#                                'abc123',database='testing')
#c = mycon.cursor()




MOVE_INCREMENT = 20
MOVES_PER_SECOND = 20
GAME_SPEED = 1000 // MOVES_PER_SECOND


class Snake(tk.Canvas):
    def __init__(self):
        super().__init__(
            width=600, height=620, background="black", highlightthickness=0)

        self.snake_positions = [(100, 100), (80, 100), (60, 100)]
        self.food_position = self.set_new_food_position()
        self.direction = "Right"

        self.score = 0

        self.load_assets()
        self.create_objects()

        self.bind_all("<Key>", self.on_key_press)

        self.grid(row=0,column=0)

        self.after(GAME_SPEED, self.perform_actions)
        

    def load_assets(self):
        try:
            self.snake_body_image = Image.open("C:/Users/Atharva Goliwar/Desktop/Snake Game/snake.png")
            self.snake_body = ImageTk.PhotoImage(self.snake_body_image)

            self.food_image = Image.open("C:/Users/Atharva Goliwar/Desktop/Snake Game/food.png")
            self.food = ImageTk.PhotoImage(self.food_image)
        except IOError as error:
            root.destroy()
            raise

    def create_objects(self):
        self.create_text(
            35, 12, text=f"Score: {self.score}", tag="score", fill="#fff", font=10
        )

        for x_position, y_position in self.snake_positions:
            self.create_image(
                x_position, y_position, image=self.snake_body, tag="snake"
            )

        self.create_image(*self.food_position, image=self.food, tag="food")
        self.create_rectangle(7, 27, 593, 613, outline="#525d69")

    def check_collisions(self):
        head_x_position, head_y_position = self.snake_positions[0]

        return (
            head_x_position in (0, 600)
            or head_y_position in (20, 620)
            or (head_x_position, head_y_position) in self.snake_positions[1:]
        )

    def check_food_collision(self):
        global GAME_SPEED
        if self.snake_positions[0] == self.food_position:
            self.score += 1
            self.snake_positions.append(self.snake_positions[-1])

            self.create_image(
                *self.snake_positions[-1], image=self.snake_body, tag="snake"
            )
            self.food_position = self.set_new_food_position()
            self.coords(self.find_withtag("food"), *self.food_position)

            score = self.find_withtag("score")
            self.itemconfigure(score, text=f"Score: {self.score}", tag="score")
            #GAME_SPEED = GAME_SPEED - 2
            print(GAME_SPEED)

    def end_game(self):
        global a
        self.delete(tk.ALL)
        self.create_text(
            self.winfo_width() / 2,
            self.winfo_height() / 2,
            text=f"Game over! You scored {self.score}!",
            fill="#fff",
            font=14
        )
        a = self.score
        '''q5 = "select score from snake_score order by score DESC"
        c.execute(q5)
        dat5 = c.fetchall()
        q1 = "select DAY(sysdate())"
        c.execute(q1)
        dat = c.fetchall()
        q3 = "select MONTH(sysdate())"
        c.execute(q3)
        dat1 = c.fetchall()
        q4 = "select YEAR(sysdate())"
        c.execute(q4)
        dat2 = c.fetchall()
        date = str(dat[0][0])+'-'+str(dat1[0][0])+'-'+str(dat2[0][0])
        print(date)
        for i in range(5):
            if dat5[i][0] < a:
                q2 = "insert into snake_score values('{}',{})".format(str(date),self.score)
                c.execute(q2)
                mycon.commit()
                break'''
        
        
    def move_snake(self):
        head_x_position, head_y_position = self.snake_positions[0]

        if self.direction == "Left":
            new_head_position = (head_x_position - MOVE_INCREMENT, head_y_position)
        elif self.direction == "Right":
            new_head_position = (head_x_position + MOVE_INCREMENT, head_y_position)
        elif self.direction == "Down":
            new_head_position = (head_x_position, head_y_position + MOVE_INCREMENT)
        elif self.direction == "Up":
            new_head_position = (head_x_position, head_y_position - MOVE_INCREMENT)

        self.snake_positions = [new_head_position] + self.snake_positions[:-1]

        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)
    def on_key_press(self, e):
        new_direction = e.keysym

        all_directions = ("Up", "Down", "Left", "Right")
        opposites = ({"Up", "Down"}, {"Left", "Right"})

        if (
            new_direction in all_directions
            and {new_direction, self.direction} not in opposites
        ):
            self.direction = new_direction

    def perform_actions(self):
        if self.check_collisions():
            global GAME_SPEED
            GAME_SPEED = 1000//15
            self.end_game()
            #self.destroy()
            #self.highscore()
            
        else:
            self.check_food_collision()
            self.move_snake()

            self.after(GAME_SPEED, self.perform_actions)

    def set_new_food_position(self):
        while True:
            x_position = randint(1, 29) * MOVE_INCREMENT
            y_position = randint(3, 30) * MOVE_INCREMENT
            food_position = (x_position, y_position)

            if food_position not in self.snake_positions:
                return food_position


root = tk.Tk()
root.title("Snake")
#root.resizable(False, False)
root.resizable(True,True)
root.tk.call("tk", "scaling", 1.5)
butt = tk.Button(root,text="Start",padx=5,pady=5,command=Snake)
butt.grid(row=0,column=1)
#board = Snake()

root.mainloop()
