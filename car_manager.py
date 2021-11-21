# Importing external packages.
import random
# Importing internal packages.
import car

# Configuration variables.
CAR_Y_POSITIONS = [0, 25, -25, 50, -50, 75, -75, 100, -100, 125, -125, 150,
                   -150, 175, -175, 200, -200, 225, -225, 250, -250]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
LIMIT_X = -320
CAR_CREATION_RATE = 6


class CarManager:

    def __init__(self):
        """Initializes the car manager."""
        self.all_cars = []
        return

    def create_new_car(self) -> None:
        """Adds a new car with random color to the array all_cars."""
        # Probably, creating a car every 6 chances.
        is_create_new_car = random.randint(1, CAR_CREATION_RATE)
        if is_create_new_car == 1:
            y_rand = random.choice(CAR_Y_POSITIONS)
            color_rand = random.choice(COLORS)
            self.all_cars.append(car.Car(car_color=color_rand, car_initial_y=y_rand))
        return

    def move_left(self) -> None:
        """Moves all cars some pixels to the left."""
        for a_car in self.all_cars:
            a_car.move_left()
            # If the car hits the left limit then it is removed from the list and the object destroyed.
            if a_car.xcor() < LIMIT_X:
                self.all_cars.remove(a_car)
                del a_car
        return

    def detect_collisions(self, the_player) -> bool:
        """Detects collisions between player and cars.\n Returns 'True' if a collision is detected."""
        for a_car in self.all_cars:
            if abs(the_player.ycor() - a_car.ycor()) < 20 and abs(a_car.xcor()) < 40:
                return True
        return False

    def increase_speed(self) -> None:
        """Increases the speed of the cars.\n
        Since the 'car_speed' is a class attribute all instances use the same value."""
        self.all_cars[0].increase_car_speed()
        return
