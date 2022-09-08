from turtle import Turtle, update

class Kachabo(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("turtle")
        self.left(90)
        self.penup()
        # self.hideturtle()
    
    def go_stating_position(self):
        self.goto(0,-260)

    def upside(self):
        self.goto(0,self.ycor()+10)
    def downside(self):
        self.goto(0,self.ycor()-10)
    

        