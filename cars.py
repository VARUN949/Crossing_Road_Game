from turtle import Turtle
import random


colors=["red","black","yellow","pink","blue","green"]
class Cars(Turtle):
    car_move=5
    carr=[]
    def __init__(self):
        super().__init__()
        self.hideturtle()
    
    def create_car(self):
        tem=random.randint(1,6)
        if tem==1:
            self.new_Car=Turtle()
            self.new_Car.penup()
            self.new_Car.shape("square")
            self.new_Car.shapesize(1,2)
            self.new_Car.color(random.choice(colors))
            self.new_Car.goto(250,random.randint(-250,250))
            self.carr.append(self.new_Car)
    
    def move_car(self):

        for i in self.carr:
            i.backward(self.car_move)

    def next_level(self,kk):
        self.car_move=2 + self.car_move
        kk.goto(0,-260)
        