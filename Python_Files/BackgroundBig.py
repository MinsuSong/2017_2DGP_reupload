from pico2d import*


class BackgroundBig:
    def __init__(self):
        self.image = load_image('Images\\Background\\Hard\\Bigmap.png')
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.width = self.image.w
        self.height = self.image.h
        self.window_bottom = 0
        self.window_left = 0

    def set_camera(self, camera):
        self.camera = camera

    def update(self, frametime):
        self.window_left = clamp(0,
                                 int(self.camera.x) - self.canvas_width//2,
                                 self.width - self.canvas_width
                                 )

        self.window_bottom = clamp(0,
                                   int(self.camera.y) - self.canvas_height//2,
                                   self.height - self.canvas_height
                                   )


    def draw(self):
        self.image.clip_draw_to_origin(
            self.window_left, self.window_bottom,
            self.canvas_width,self.canvas_height,
            0,0
        )



