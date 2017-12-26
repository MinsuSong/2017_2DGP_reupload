from pico2d import*
import random

class ObstacleHill:
    image = None

    width = 100 / 2
    height = 200 / 2


    def __init__(self, x):
        self.x = x
        self.y = 100 + self.height
        if self.image == None:
            self.image = load_image('Images\Object\Obstacle\obstaclehill.png')

    def set_background(self, background):
        self.background = background


    def draw(self):
        self.image.draw(self.x - self.background.window_left,
                        self.y - self.background.window_bottom,
                        self.width*2, self.height*2)

    def get_bb(self):
        return self.x - self.width - self.background.window_left,\
               self.y - self.height - self.background.window_bottom,\
               self.x + self.width - self.background.window_left,\
               self.y + self.height - self.background.window_bottom

