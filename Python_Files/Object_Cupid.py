from pico2d import*

class Cupid:
    image = None

    width = 27/2
    height = 25/2

    time_per_action = 0.2
    action_per_time = 1 / time_per_action
    frame_per_action = 1

    def __init__(self):
        self.x = 50
        self.y = 100 + self.height
        self.frame = 0
        self.total_frames = 0
        if self.image == None:
            self.image = load_image('Cupid_Stand.png')


    def draw(self):
        self.image.clip_draw(self.frame*27, 0, 27, 25, self.x, self.y)

    def update(self, frame_time):
        self.total_frames += Cupid.frame_per_action * Cupid.action_per_time * frame_time
        self.frame = int(self.total_frames) % 6

    def get_bb(self):
        return self.x - self.width, self.y - self.height, self.x + self.width, self.y + self.height

    def draw_bb(self):
        draw_rectangle(*self.get_bb())