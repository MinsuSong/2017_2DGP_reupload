from pico2d import*

class Life:
    font = None

    def __init__(self):
        self.x = 0
        self.y = 730
        self.lifepoint = 10
        Life.font = load_font('font\\ENCR10B.TTF', 30)

    def decrease(self):
        self.lifepoint -= 1

    def draw(self):
        Life.font.draw(self.x, self.y, 'Life:%d' %self.lifepoint, (255,255,255))