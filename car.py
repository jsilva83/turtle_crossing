# Importing external packages.
import turtle
# Global constants.
MOVE_INCREMENT = 10


class Car(turtle.Turtle):
    # Extended class attributes.
    car_speed = MOVE_INCREMENT

    def __init__(self, car_color, car_initial_y):
        super().__init__()
        # Turtle attributes and methods.
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(car_color)
        self.penup()
        self.setheading(180)
        self.goto((280, car_initial_y))
        return

    def move_left(self) -> None:
        self.forward(self.car_speed)
        return

    def increase_car_speed(self) -> None:
        Car.car_speed += MOVE_INCREMENT
        return
