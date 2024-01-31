import turtle as tu
import snake
import time

x=0
y=0
coordinates= [(x,y),(x-20,y),(x-40,y)]

screen1=tu.Screen()

game_is_on=True

for x in coordinates:
    piece=snake.Snake(x)

while game_is_on==True:
    screen1.update()
    time.sleep(0.1)
    piece.move()






screen1.exitonclick()