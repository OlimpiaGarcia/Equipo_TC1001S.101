from turtle import pencolor
from turtle import up
from turtle import goto
from turtle import down
from turtle import circle
from turtle import update
from turtle import setup
from turtle import tracer
from turtle import hideturtle
from turtle import done
from turtle import onscreenclick

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


def occupied(x, y, casillas):
    """Verifies if the box is occupied"""
    if x == -200.0 and y == 66.0:
        if casillas[0] is False:
            casillas[0] = True
        else:
            return True
    if x == -67.0 and y == 66.0:
        if casillas[1] is False:
            casillas[1] = True
        else:
            return True
    if x == 66.0 and y == 66.0:
        if casillas[2] is False:
            casillas[2] = True
        else:
            return True
    if x == -200.0 and y == -67.0:
        if casillas[3] is False:
            casillas[3] = True
        else:
            return True
    if x == -67.0 and y == -67.0:
        if casillas[4] is False:
            casillas[4] = True
        else:
            return True
    if x == 66.0 and y == -67.0:
        if casillas[5] is False:
            casillas[5] = True
        else:
            return True
    if x == -200.0 and y == -200.0:
        if casillas[6] is False:
            casillas[6] = True
        else:
            return True
    if x == -67.0 and y == -200.0:
        if casillas[7] is False:
            casillas[7] = True
        else:
            return True
    if x == 66.0 and y == -200.0:
        if casillas[8] is False:
            casillas[8] = True
        else:
            return True


state = {'player': 0}
players = [drawx, drawo]
"""This list saves the state of boxes"""
casillas = []
num_casillas = 9
for i in range(num_casillas):
    casillas.append(False)


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    occ = occupied(x, y, casillas)
    if occ is True:
        return
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
"""Draws the grid"""
grid()
"""Updates the drawings when is required"""
update()
"""Captures the mouse click"""
onscreenclick(tap)
done()
