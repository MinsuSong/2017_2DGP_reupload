from pico2d import *

class ButtonNormal:
    width = 200 / 2
    height = 100 / 2

    def __init__(self):
        self.x = 680
        self.y = 450
        self.image = load_image('Images\Interface\Button\Button_Normal.png')
        self.imageActive = load_image('Images\Interface\Button\Button_Normal_Active.png')


    def draw(self, collide):
        if collide is True:
            self.imageActive.draw(self.x, self.y)

        else:
            self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height

    def draw_bb(self):
        draw_rectangle(*self.get_bb())