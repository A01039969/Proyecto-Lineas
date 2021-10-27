'Actividad 2 - Snake'
'Equipo 5'
'Marcelo Durán A01720893'
'Rodolfo Sandoval A01720253'
'Eduardo De La Rosa A0103996'
'Alejandro Gonzalez A01570396'
'Paola De La Rosa A01233794'

"""Snake, classic arcade game."""

from random import randrange, choice
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ['green','yellow','black','blue','pink']
snakeColor = choice(colors)
colors.remove(snakeColor)
foodColor = choice(colors)



def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def foodMove():
    test = [-10,0,10]
    random_move = test[randrange(0,3)]
    random_move2 = test[randrange(0,3)]
    foodTest = vector(food.x + random_move, food.y + random_move2)
    
    while(not inside(foodTest)):
        random_move = test[randrange(0,3)]
        random_move2 = test[randrange(0,3)]
        foodTest = vector(food.x + random_move, food.y + random_move2)
        
    food.x = food.x + random_move
    food.y = food.y + random_move2

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food or food in snake:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        rnumber = randrange(0, 100)
        if(90 < rnumber):
            foodMove()

        
    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
        
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
