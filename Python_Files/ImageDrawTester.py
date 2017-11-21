from pico2d import*

open_canvas(1500, 750)


global running


class Background_Forest:
    width = 1500
    height = 750

    def __init__(self):
        self.x = 750
        self.y = 375
        self.image = load_image('Background.png')

    def draw(self):
        self.image.draw(self.x, self.y)

class Cupid:
    def __init__(self):
        self.x = 10
        self.y = 100
        self.frame = 0
        self.image = load_image('Cupid_Stand.png')

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(self.frame*27, 0, 27, 25, self.x, self.y)

def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type ==  SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

cupid = Cupid()
running = True
background = Background_Forest()

while (running):
    handle_events()
    clear_canvas()
    background.draw()
    cupid.draw()
    cupid.update()

    update_canvas()
    delay(0.05)
