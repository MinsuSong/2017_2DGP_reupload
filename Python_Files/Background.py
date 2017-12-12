from pico2d import*

class Background_Forest:

    width = 1500
    height = 750


    def __init__(self):
        self.x = 750
        self.y = 375
        self.bgm = load_music('sound\\football.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.image = load_image('Images\\Background\\Normal\\background.png')


    def draw(self):
        self.image.draw(self.x, self.y)
