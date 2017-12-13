from pico2d import*
import random

class ObstacleHill:
    image = None

    width = 60 / 2
    height = 200 / 2


    def __init__(self, x):
        self.x = x
        self.y = 100 + self.height
        if self.image == None:
            self.image = load_image('Images\Object\Obstacle\obstaclehill.png')

    def draw(self):
        self.image.draw(self.x, self.y, self.width*2, self.height*2)

    def get_bb(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

