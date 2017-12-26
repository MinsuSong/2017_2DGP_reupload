from pico2d import*

class Cupid:
    image = None

    width = 27/2
    height = 25/2

    time_per_action = 0.2
    action_per_time = 1 / time_per_action
    frame_per_action = 1

    def __init__(self):
        self.x = 60
        self.y = 100
        self.frame = 0
        self.total_frames = 0
        if self.image == None:
            self.image = load_image('Images\Object\Character\Cupid_Stand.png')

    def set_background(self, background):
        self.background = background

    def draw(self):
        self.image.clip_draw(self.frame * 27, 0, 27, 25, self.x - self.background.window_left,
                             self.y - self.background.window_bottom)

    def get_bb(self):
        return self.x - self.width - self.background.window_left, \
               self.y - self.height - self.background.window_bottom, \
               self.x + self.width - self.background.window_left, \
               self.y + self.height - self.background.window_bottom


    def update(self, frame_time):
        self.total_frames += Cupid.frame_per_action * Cupid.action_per_time * frame_time
        self.frame = int(self.total_frames) % 6

