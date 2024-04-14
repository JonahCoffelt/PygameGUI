import pygame as pg
import sys

from ui_handler import UI_Handler

pg.init()

class App:
    def __init__(self):
        self.win_size = (900, 600)
        self.win = pg.display.set_mode(self.win_size, pg.RESIZABLE)
        self.clock = pg.time.Clock()

        self.ui_handler = UI_Handler(self.win_size)

    def update(self):
        self.ui_handler.update()

    def draw(self):
        if self.ui_handler.update_texture == 0 or self.ui_handler.update_texture == 1: 
            self.win.fill((255, 255, 255))
            self.win.blit(self.ui_handler.surf, (0, 0))

        pg.display.flip()

    def start(self):
        while True:
            self.clock.tick()
            pg.display.set_caption(str(round(self.clock.get_fps())))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

                if event.type == pg.VIDEORESIZE:
                    self.ui_handler.update_texture = 2
                    self.ui_handler.win_size = (event.w, event.h)
                    self.ui_handler.surf = pg.Surface((event.w, event.h)).convert_alpha()

            self.update()
            self.draw()

app = App()
app.start()