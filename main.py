import turtle as tu
import snake
import time

x=0
y=0


screen1=tu.Screen()
screen1.tracer(0)
screen1.listen()

snake1=snake.Snake()

screen1.onkey(snake1.move_up,"Up")


game_is_on=True

while game_is_on==True:
    screen1.update()
    time.sleep(0.5)
    # print(snake1.list[0].xcor(),snake1.list[0].ycor())
    snake1.move()
    # snake1.move_up()


screen1.exitonclick()