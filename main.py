from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakey the snake")
screen.tracer(0)

snakey = Snake()

food = Food()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(snakey.up, "Up")
screen.onkey(snakey.down, "Down")
screen.onkey(snakey.left, "Left")
screen.onkey(snakey.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snakey.move()

    # Detect collision with food
    if snakey.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_scoreboard()
        snakey.extend()

    # Detect collision with wall
    if snakey.head.xcor() > 280 or snakey.head.xcor() < -280 or snakey.head.ycor() > 280 or snakey.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snakey.segments[1:]:
        if snakey.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
