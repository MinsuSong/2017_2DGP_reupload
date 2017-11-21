from pico2d import*

class Target:
    image = None

    width = 60 / 2
    height = 60 / 2
    def __init__(self):
        self.x = 1450
        self.y = 100 + self.height
        if self.image == None:
            self.image = load_image('Target_TEMP.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height

    def draw_bb(self):
        draw_rectangle(*self.get_bb())