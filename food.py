import random
from turtle import Turtle

x_cor = random.randrange(-250, 250)
y_cor = random.randrange(-250, 250)

class Food:

    def __init__(self):
        food=Turtle()
        food.shape("circle")
        food.penup()
        food.color("black")
        self.xcor=x_cor
        self.ycor=y_cor
        # self.reset_food()
        food.goto(x_cor, y_cor)
        self.foodx=food

    def reset(self):
        x_cor1 = random.randrange(-250, 250)
        y_cor1 = random.randrange(-250, 250)
        self.foodx.goto(x_cor1,y_cor1)






