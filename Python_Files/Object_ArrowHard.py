from pico2d import*


class Arrow:
    image = None
    firesound = None
    hitsound = None
    width = 20 / 2
    height = 20 / 2

    def __init__(self, power):
        #위치
        self.position_X = 60
        self.position_Y = 125
        #힘
        self.power = power
        #속도
        self.velocity_X = self.power * 10
        self.velocity_Y = self.power * 10
        #가속도
        self.accelation_X = 0
        self.accelation_Y = -500


        Arrow.image = load_image('Images\\Object\\Arrow\\Arrow_TEMP.png')

        if Arrow.firesound == None:
            Arrow.firesound = load_wav('sound\\sound_shot.wav')
            Arrow.firesound.set_volume(64)


        if Arrow.hitsound == None:
            Arrow.hitsound = load_wav('sound\\sound_hit.wav')
            Arrow.hitsound.set_volume(64)

    def set_background(self, background):
        self.background = background

    def draw(self,frame_time):
        self.image.draw(
                            self.position_X - self.background.window_left,
                            self.position_Y - self.background.window_bottom
        )




    def update(self,frame_time):
        self.velocity_X = self.velocity_X + self.accelation_X * frame_time
        self.velocity_Y = self.velocity_Y + self.accelation_Y * frame_time

        self.position_X = self.position_X + frame_time * self.velocity_X
        self.position_Y = self.position_Y + frame_time * self.velocity_Y


    def get_bb(self):
        return self.position_X - Arrow.width -self.background.window_left,\
               self.position_Y - Arrow.height - self.background.window_bottom,\
               self.position_X + Arrow.width - self.background.window_left,\
               self.position_Y + Arrow.height - self.background.window_bottom

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def firearrow(self):
        self.firesound.play()

    def hit(self):
        self.hitsound.play()