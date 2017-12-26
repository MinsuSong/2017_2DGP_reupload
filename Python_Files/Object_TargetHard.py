from pico2d import*

class Target:
    image = None

    width = 60 / 2
    height = 60 / 2
    def __init__(self):
        self.x = 3500
        self.y = 100 + self.height
        if self.image == None:
            self.image = load_image('Images\Object\Target\Target_TEMP.png')

    def draw(self):
        self.image.draw(self.x, self.y)


    def draw(self):
        self.image.draw(
                            self.x - self.background.window_left,
                            self.y - self.background.window_bottom
                        )

    def set_background(self, background):
        self.background = background

    def get_bb(self):
        return self.x - self.width - self.background.window_left,\
               self.y - self.height - self.background.window_bottom,\
               self.x + self.width - self.background.window_left,\
               self.y + self.height - self.background.window_bottom
