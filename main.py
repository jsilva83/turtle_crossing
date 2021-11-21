# Importing external packages
import time
from turtle import Screen
# Importing internal packages
import scoreboard
from player import Player
from car_manager import CarManager

# Configuration variables.
INITIAL_SPEED = 0.05

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)
screen.title('Turtle crosses the street1')
# Initialize player.
my_player = Player()
# Initialize car manager.
my_car_manager = CarManager()
# Initialize scoreboard.
my_scoreboard = scoreboard.Scoreboard()
# Screen is listening to keys pressed by player.
screen.listen()
screen.onkeypress(fun=my_player.move_up, key='Up')
# Start moving the game.
game_is_on = True
while game_is_on:
    time.sleep(INITIAL_SPEED)
    # Create a car every 6 cycles.
    my_car_manager.create_new_car()
    my_car_manager.move_left()
    screen.update()
    # detect collisions between player and cars.
    if my_car_manager.detect_collisions(my_player):
        game_is_on = False
    if my_player.is_at_top():
        my_scoreboard.increment_score()
        my_player.reset_position()
        my_car_manager.increase_speed()
# Game over.
my_scoreboard.game_over()
screen.exitonclick()
