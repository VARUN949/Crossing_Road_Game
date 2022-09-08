from turtle import Turtle

class Scor_car_crossing(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level=0
        self.penup()
        self.goto(-250,250)
        self.write(f"Level : {self.level}",font=('Arial', 22, 'normal'),align="left")
        self.penup()

    def pp(self):
        self.clear()
        self.write(f"Level : {self.level}",font=('Arial', 22, 'normal'),align="left")

    def incre_scor(self):
        self.level+=1
        self.pp()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over",font=('Arial', 21, 'normal'),align="center")
        self.goto(0,-35)
        self.write(f"Your Score is {self.level}",font=('Arial', 21, 'normal'),align="center")
        
        
        