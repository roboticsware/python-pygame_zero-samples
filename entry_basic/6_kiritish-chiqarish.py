from pgzhelper import *

WIDTH = 960
HEIGHT = 540

xazina = Actor("xazina_sandig'i", (WIDTH / 2, HEIGHT / 2))
xazina.images = ["xazina_sandig'i", "xazina_sandig'i_o"]

input_text = ""
input_done = False
input_rect = Rect(350, 450, 200, 50)

guide_rect = Rect(300, 50, 400, 50)
parol = "1234"


def draw():
    screen.blit("cho'l", (0, 0))
    xazina.draw()
    
    # Tushuntirish textbox
    screen.draw.filled_rect(guide_rect, 'black')
    if input_done:
        if input_text == password:
            screen.draw.textbox("Xazinaga ega bo'ldingiz!", guide_rect)
        else:
            screen.draw.textbox("Oishga muvaffaqiyatsizlik!", guide_rect)

        pygame.display.update()
        game.exit()
    else:
        screen.draw.textbox("Parolingizni kiriting.", guide_rect)

    # Input textbox
    screen.draw.filled_rect(input_rect,'pink')
    screen.draw.textbox(input_text, input_rect)


def update():
    if input_done:
        if input_text == parol:
            treasure.sel_image("xazina_sandig'i_o")
            sounds.olqish.play()
        else:
            sounds.xavf_ogohlantirish.play()


def on_key_down(key, unicode):
    global input_text, input_done

    if key == keys.RETURN:
        input_done = True
    elif key == keys.BACKSPACE:
        input_text = input_text[:-1]
    else:
        input_text += unicode
