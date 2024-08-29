from turtle import Turtle,Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
screen.listen()
screen.onkey(player.go_up, "Up")
game_is_on = True
scoreboard=Scoreboard()

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()


    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on=False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.inc_level()


screen.exitonclick()