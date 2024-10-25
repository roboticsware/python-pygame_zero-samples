import random
from pgzhelper import *

TITLE = "Flappy Bird"
WIDTH = 400
HEIGHT = 708

GRAVITY = 0.3
drop_speed = 0
GAP = 140  # Trubalarning orasidagi bo'sh joyining uzunligi
bird_alive = True
score = 0
PIPE_SPEED = 3

# O'yinning aktyotrlarning obyektini yaratish
flappy_bird = Actor('bird1', (75, 350))
flappy_bird.images = ['bird0', 'bird1', 'bird2']
flappy_bird.fps = 10
top_pipe = Actor('top', (350, 0))
bottom_pipe = Actor('bottom', (350, top_pipe.height + GAP))

def draw():
    screen.blit('background', (0, 0))
    flappy_bird.draw()
    top_pipe.draw()
    bottom_pipe.draw()
    
    # Ekranda balni ko'rsatish
    screen.draw.text(
        str(score),
        color = 'white',
        midtop = (WIDTH / 2, 10),
        fontsize = 70,
        shadow = (1, 1)
    )
    
# Trubalarning joylashuvini qaytadan sizlash
def reset_pipes():
    random_y =  random.randint(-100, 100)
    top_pipe.y = random_y
    bottom_pipe.y = top_pipe.height + GAP + random_y
    top_pipe.x = WIDTH
    bottom_pipe.x = WIDTH

def update():
    global drop_speed, bird_alive, score
    drop_speed += GRAVITY
    flappy_bird.y += drop_speed
    if bird_alive == True:
        flappy_bird.animate()

    top_pipe.x -= PIPE_SPEED
    bottom_pipe.x -= PIPE_SPEED

    # Trubalarning taqrorlashi
    if top_pipe.right < 0 or top_pipe.right < 0:
        reset_pipes()
        if bird_alive == True:
            score += 1

    # Trubalar bilan to'qnashuv
    if flappy_bird.colliderect(top_pipe) or flappy_bird.colliderect(bottom_pipe):
        flappy_bird.image = "birddead"
        bird_alive = False
        
    # O'yining qaytadan boshlanishi
    if flappy_bird.y > HEIGHT or flappy_bird.y < 0 :
        flappy_bird.image = 'bird1'
        bird_alive = True
        flappy_bird.center = (75, 350)
        drop_speed = 0
        reset_pipes()
        score = 0

# Sichqoncha yoki probel bosganda yuqoriga uchib ketadi
def on_mouse_down():
    global drop_speed
    if bird_alive == True:
        drop_speed = -5

def on_key_down():
    global drop_speed
    if bird_alive == True:
        drop_speed = -5
