from pico2d import*

class Mouse:
    width = 10 / 2
    height = 10 / 2

    def __init__(self):
        self.x = 0
        self.y = 0

    def get_bb(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height


    def get_mouse_position(self,mouse_X, mouse_Y):
        self.x, self.y = mouse_X, mouse_Y