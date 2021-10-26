from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circulo(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    "Native function from Turtle which lets you make a circle, add the parameter which is the radius."
    circle(50)
    
    end_fill()
    
    
def rectangle(start, end):
    "Draw rectangle from start to end. Multiply the horizontal distance of a square to create a rectangle."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(2*(end.x - start.x))
        left(90)
        forward(end.x - start.x)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw a triangle. Iterate each side with a 120 angle to create 3 lines forming all 360 degrees of an equilateral triangle."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range(3):
        forward(end.x - start.x)
        left(180-60)
        
    end_fill()
    

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None
        
def store(key, value):
    "Store value in state at key."
    state[key] = value
    
def store_color(iColor):
    "Choose the color of the "
    colour = state['store_color']
    
    if colour is None:
        color('black','black')
    else:
        color(iColor, iColor)

state = {'start': None, 'shape': line, 'store_color': 'blue'}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: store_color('black'), 'K')
onkey(lambda: store_color('white'), 'W')
onkey(lambda: store_color('green'), 'G')
onkey(lambda: store_color('blue'), 'B')
onkey(lambda: store_color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circulo), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()