"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

"""Importar librerias"""

from turtle import up, goto, down
from turtle import color, begin_fill, forward
from turtle import left, end_fill, clear
from turtle import shape, stamp, write
from turtle import update, ontimer
from turtle import setup, addshape, hideturtle
from turtle import tracer, onscreenclick, done

from random import shuffle

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64

"""Definir variables globales"""

cont = 0
COUNT = 0

def increment():
    global cont
    cont +=1

def secincrement():
    global COUNT
    COUNT +=1


"""Draw white square with black outline at (x, y)."""

def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

"""Convert (x, y) coordinates to tiles index."""

def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

"""Convert tiles count to (x, y) coordinates."""

def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

"""Update mark and hidden tiles based on tap."""

def tap(x, y):
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        secincrement()
        print("Number of try", COUNT)
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        increment()
        print(cont)

"""Draw image and tiles."""

def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    if COUNT > 100:
        clear()
        color("Red")
        goto(0, 0)
        write("Game Over", align = "center", font = ("Arial", 30 , "bold"))
        goto("0, -50")
        done()
        exit()
    
    if cont == 32:
        clear()
        color("Red")
        goto(0, 0)
        write('Victory', align = "center", font = ("Arial", 30, "bold"))
        goto(0, -50)
        done()
        exit()
    
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
