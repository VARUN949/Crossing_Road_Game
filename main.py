from turtle import Turtle,Screen
from kachabo import Kachabo
import time
from level import Scor_car_crossing
from cars import Cars


scor=Scor_car_crossing()
ss=Screen()
ss.tracer(0)
ss.setup(600,600)
kk=Kachabo()
car=Cars()
kk.go_stating_position()
ss.update()

ss.listen()
ss.onkey(key="Down",fun=kk.downside)

game_is=True
while game_is:
    time.sleep(0.1)
    ss.onkey(key="Up",fun=kk.upside)
    car.create_car()
    car.move_car()
    ss.update()
    for i in car.carr:
        if i.distance(kk)<20:
            scor.game_over()
            game_is=False
    if kk.ycor()>270:
        car.next_level(kk)
        scor.incre_scor()
        


ss.exitonclick()