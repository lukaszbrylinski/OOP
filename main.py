from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

food = Food()

score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    '#Detect collision with food'
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_game()
        snake.reset()

    #Detect collision with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            score.reset_game()
            snake.reset()

screen.exitonclick()
