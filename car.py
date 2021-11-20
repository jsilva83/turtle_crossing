# Importing external packages.
import turtle


class Car(turtle.Turtle):

    def __init__(self, car_color):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(car_color)
        self.penup()
        self.goto((280, 0))
        return
