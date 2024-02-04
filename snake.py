import turtle as tu
x=0
y=0
coordinates= [(x,y),(x-20,y),(x-40,y),(x-60,y)]
# coordinates= [(x,y),(x-20,y),(x-40,y),(x-60,y),(x-80,y),(x-100,y)]
# jh: to check if my logic works with longer snake

class Snake():
    def __init__(self):
        self.list=[]
        self.starting_pieces()

    def create_piece(self):
        tu1 = tu.Turtle()
        tu1.shape("square")
        tu1.color("blue")
        tu1.penup()
        return tu1

    def starting_pieces(self):
        for cords in coordinates:
            tu2=self.create_piece()
            tu2.goto(cords)
            self.list.append(tu2)

    def move(self):
        for x in range(0,len(self.list)): #Angela did it differently by moving the last piece first.
            # I am focused on the first piece first, and the second and so on.
            if x== 0:
                curr_x = self.list[x].xcor()
                curr_y = self.list[x].ycor()
                self.list[x].forward(20)
            elif (x % 2)==1:
                curr_x2 = self.list[x].xcor()
                curr_y2 = self.list[x].ycor()
                self.list[x].goto(curr_x, curr_y)
            elif (x % 2)==0:
                curr_x = self.list[x].xcor()
                curr_y = self.list[x].ycor()
                self.list[x].goto(curr_x2, curr_y2)
        #JH: why I used the above? It was based on the pattern of locations/variables. Except the first (index 0),
        # the even and odd indexes shared a pattern. See the picture in the project.


    def after_food(self):
        x=self.list[-1].xcor()
        y=self.list[-1].ycor()
        tu3=self.create_piece()
        tu3.goto(x,y)
        self.list.append(tu3)


    def move_up(self):
        # print (self.list[0].heading())
        if self.list[0].heading() ==0:
            self.list[0].left(90)
        elif self.list[0].heading() == 180:
            self.list[0].right(90)

    def move_down(self):
        # print (self.list[0].heading())
        if self.list[0].heading() ==0:
            self.list[0].right(90)
        elif self.list[0].heading() == 180:
            self.list[0].left(90)

    def move_right(self):
        # print (self.list[0].heading())
        if self.list[0].heading() == 90:
            self.list[0].right(90)
        elif self.list[0].heading() == 270:
            self.list[0].left(90)

    def move_left(self):
        # print (self.list[0].heading())
        if self.list[0].heading() == 90:
            self.list[0].left(90)
        elif self.list[0].heading() == 270:
            self.list[0].right(90)