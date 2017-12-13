from pico2d import*

class ground:


    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = load_image('Images\\Background\\Normal\\background.png')

    def draw(self):
        self.image.draw(self.x, self.y)