from turtle import Turtle
import random
colors=["red","green","orange","blue","purple"]
Move_inc = 10
starting_move_dis = 5
class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.carspeed=starting_move_dis

    def create_car(self):
        random_chance=random.randint(1,6)
        if random_chance == 1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(colors))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed+= Move_inc