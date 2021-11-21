# Importing external packages.
import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(turtle.Turtle):

    def __init__(self):
        """Initializes the player object and places it at the initial position"""
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.reset_position()
        return

    def move_up(self) -> None:
        """Moves the player up if the user presses the up key"""
        if self.ycor() < FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
        return

    def is_at_top(self) -> bool:
        """Checks if the player is at the top of the screen.\nReturns 'True' if at the top edge."""
        if self.ycor() == FINISH_LINE_Y:
            return True
        return False

    def reset_position(self) -> None:
        """Places the player back at the initial position."""
        self.goto(STARTING_POSITION)
        return
