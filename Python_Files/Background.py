from pico2d import*

class Background_Forest:

    width = 1500
    height = 750


    def __init__(self):
        self.x = 750
        self.y = 375
        self.image = load_image('Images\\Background\\Normal\\background.png')


    def draw(self):
        self.image.draw(self.x, self.y)
