from turtle import *
from freegames import vector
    
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