import random
from turtle import Turtle

x_cord=random.randrange(-250,250)
y_cord=random.randrange(-250,250)

class Food:

    def __init__(self):
        food=Turtle()
        food.shape("circle")
        food.penup()
        food.color("black")
        food.goto(x_cord,y_cord)
        self.xcor=x_cord
