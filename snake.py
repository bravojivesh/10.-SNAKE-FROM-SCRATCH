import turtle as tu
x=0
y=0
coordinates= [(x,y),(x-20,y),(x-40,y)]

class Snake():
    def __init__(self):
        self.list=[]
        self.starting_pieces()

    def starting_pieces(self):
        for x in coordinates:
            tu1 = tu.Turtle()
            tu1.shape("square")
            tu1.color("blue")
            tu1.penup()
            tu1.goto(x)
            self.list.append(tu1)

    def move(self):
        self.list[0].forward(20)
        # print (self.list[1],self.list[2])
        # print (len(self.list))
        for x in range(1,len(self.list)):
            goto_x= self.list[x-1].xcor()-20
            goto_y=self.list[x-1].ycor()
            # print ("x",goto_x, goto_y)
            self.list[x].goto(goto_x,goto_y)
            # print (x)

    def move_up(self):
        self.list[0].left(90)
        # self.list[0].forward(20)





