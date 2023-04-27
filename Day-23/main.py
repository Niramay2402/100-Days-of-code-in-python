import time
from turtle import Screen
from player import Player, FinishLine
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level = Scoreboard()
FL = FinishLine()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
FL.draw_fl()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    if player.ycor() == 240:
        player.lvl_update()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            level.game_over()



screen.exitonclick()
