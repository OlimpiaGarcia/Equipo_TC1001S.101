from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    pencolor('red')
    line(x+40, y+40, x + 100, y + 100)
    line(x+40, y + 100, x + 100, y+40)


def drawo(x, y):
    """Draw O player."""
    pencolor('blue')
    up()
    goto(x + 67, y + 40)
    down()
    circle(30)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player

"""Size of the window"""
setup(420, 420, 370, 0)
"""Hides the turtle that draws the things in the program"""
hideturtle()
"""Quits the tracer animation"""
tracer(False)
grid()
update()
onscreenclick(tap)
done()