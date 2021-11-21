# Import external packages.
import turtle

# Global constants.
FONT = ("Courier", 24, "normal")
COLOR = 'black'
POSITION = (-280, 270)


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLOR)
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.score = -1
        self.increment_score()
        return

    def increment_score(self) -> None:
        self.clear()
        self.score += 1
        self.write(f'Score: {self.score}', align='left', font=FONT)
        return

    def game_over(self) -> None:
        self.goto((0, 0))
        self.write(f'GAME OVER', align='center', font=FONT)
        return
