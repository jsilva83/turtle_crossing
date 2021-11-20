# Importing external packages
import time
from turtle import Screen
# Importing internal packages
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import car

# Initialize screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)
# Initialize player
my_player = Player()
# Screen is listening to keys pressed by player.
screen.listen()
screen.onkeypress(fun=my_player.move_up, key='Up')
# Start moving the game
# Create car
my_car = car.Car('red')
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
