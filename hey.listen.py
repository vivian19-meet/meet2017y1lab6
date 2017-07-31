UP_ARROW='UP'
LEFT_ARROW='Left'
RIGHT_ARROW='Right'
DOWN_AROW='Down'
SPACER='space'
up=0
Left=1
Right=2
Down=3
direction=up
def up():
    global direction
    direction=up
    print('the button pressed!')
def Down():
    global direction
    direction=Down
    print('the button pressed!')
def Right():
    global direction
    direction=Right
    print('the button pressed!')
def Left():
    global direction
    direction=Left
    print('the button pressed!')
