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
    time.sleep(0.1)
    # print(snake1.list[0].xcor(),snake1.list[0].ycor())
    snake1.move()

    # x_diff= abs(abs(snake1.list[0].xcor()) - abs(food1.xcor)) #tracking xcor difference of the food and snake
    # y_diff=abs(abs(snake1.list[0].ycor()) - abs(food1.ycor)) #tracking ycor difference of the food and snake
    #
    # print(f"snake x is: {abs(snake1.list[0].xcor())} and snake y is:{abs(snake1.list[0].ycor())}")
    # print (f"food x is: {abs(food1.xcor)} and food y is {abs(food1.ycor)} ")

    if (snake1.list[0].distance(food1.foodx) < 30): #detect collision with the food
        print ("asdasdas")
        snake1.after_food()
        food1.reset()

    for snake_object in snake1.list: #detect collision with its own body
        if snake_object== snake1.list[0]:
            pass
        elif snake_object.distance(snake1.list[0]) <10:
            print ("121212")
            game_is_on= False
  

screen1.exitonclick()