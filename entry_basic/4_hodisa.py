from pgzhelper import *

WIDTH = 960
HEIGHT = 540

drawing = False

qalam = Actor('qalam', (WIDTH / 2, HEIGHT / 2), anchor=('left', 'bottom'))
qalam.scale = 0.3
qalam.pen_init((WIDTH, HEIGHT))
eraser = Actor("o'chirg'ich", (900, 50))
eraser.scale = 0.5

def draw():
    screen.fill('white')
    pencil.brush_draw()
    pencil.draw()
    eraser.draw()
    
    if drawing is False:
        pencil.brush_stop()

def on_mouse_move(pos):
    pencil.left, pencil.bottom = pos

def on_mouse_down(pos):
    global drawing
    drawing = True

    if eraser.collidepoint_pixel(pos):
        pencil.brush_clear()

def on_mouse_up():
    global drawing
    drawing = False
