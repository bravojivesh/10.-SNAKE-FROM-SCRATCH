import turtle as tu


class Snake(tu.Turtle):

    def __init__(self,x):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("blue")
        self.goto(x)


    def move(self):
        self.forward(20)


