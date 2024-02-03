import turtle as tu
import snake
import time
import food

x=0
y=0


screen1=tu.Screen()
screen1.tracer(0)
screen1.listen()
# print (screen1.window_width())
# print (screen1.window_height())


snake1=snake.Snake()
food1=food.Food()

screen1.onkey(snake1.move_up,"Up")
screen1.onkey(snake1.move_down,"Down")
screen1.onkey(snake1.move_right,"Right")
screen1.onkey(snake1.move_left,"Left")

game_is_on=True

while game_is_on==True:
    screen1.update()
    time.sleep(0.5)
    # print(snake1.list[0].xcor(),snake1.list[0].ycor())
    snake1.move()

    print(snake1.list[0].xcor(),food1.xcor )
    print(abs((snake1.list[0].xcor) - (food1.xcor)))

    if (abs(snake1.list[0].xcor()- food1.xcor))<= 5:
        print ("asdasdas")
        game_is_on=False





screen1.exitonclick()