# Importing external packages.
import turtle

# Configuration variables.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(turtle.Turtle):

    def __init__(self):
        """Initializes the car manager"""
