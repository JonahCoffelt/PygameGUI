import pygame as pg
import numpy as np
import random
from text_handler import TextHandler
from ui_screen_data import ScreenData

assets = {'btn_blank' : 'button_blank.png',
          'btn' : 'button.png'}

class UI_Handler:
    def __init__(self, win_size=(900, 600)):
        self.win_size = win_size
        self.surf = pg.Surface(win_size).convert_alpha()
        self.text_handler = TextHandler()
        self.screen_data = ScreenData(self).screen_data

        self.assets = {asset : pg.image.load(f'UI_Assets/{assets[asset]}').convert_alpha() for asset in assets}
        self.values = {
            'volume' : 5.0,
            'FOV' : 90.0,
            'render_distance' : 10,
            'view_distance' : 250,
            'lighting_distance' : 50
            }
        self.mouse_states = [False, False, False]

        self.screen = self.pause
        data = self.screen_data[self.screen]
        self.current_screen_data = {key : value.copy() for key, value in zip(data.keys(), data.values())}

        self.update_texture = 2
        self.n_cards = 5

    def update(self):
        # Handles all keyboard and mouse input for UI
        self.mouse_pos = pg.mouse.get_pos()
        self.mouse_buttons = pg.mouse.get_pressed()
        self.keys = pg.key.get_just_pressed()
        self.update_elements()
        self.mouse_states = [state for state in self.mouse_buttons]

        # Calls the function of the current screen
        self.screen()

        # Used to limit the number of draw calls
        if self.update_texture >= 0: self.update_texture -= 1


    def draw(self):
        if not(self.update_texture == 0 or self.update_texture == 1 or self.update_texture == 2): return
        self.execute_draw_calls()
        self.draw_images()
        self.draw_sliders()
        self.draw_text()

    def update_elements(self):
        self.update_hotkeys()
        self.update_buttons()
        self.update_sliders()

    def log(self, txt=''):
        print(txt)
        self.update_texture = 2

    def set_screen(self, screen):
        self.update_texture = 2
        self.screen = screen
        data = self.screen_data[screen]
        self.current_screen_data = {key : value.copy() for key, value in zip(data.keys(), data.values())}
    
    def add_button(self, pos: tuple=(.5, .5, .1, .1), img: pg.image=None, func=None, args: list=[]):
        if pos == "rndm": pos = np.array([random.uniform(0, 1), random.uniform(0, 1), .1, .1])
        self.current_screen_data['buttons'].append([np.array([*pos]), img, func, [*args]])
    
    def get_rect(self, element):
        win_scale = np.array([self.win_size[0], self.win_size[1], self.win_size[0], self.win_size[1]])
        rect = (element[0] * win_scale)
        rect[0] -= rect[2]/2
        rect[1] -= rect[3]/2

        if 0.0 in rect[2:]:
            index = np.where(rect==0.0)[0][0]
            img_rect = self.assets[element[1]].get_rect()
            if index == 2:
                rect[2] = rect[3] * (img_rect[2] / img_rect[3])
                rect[0] -= rect[2]/2
            if index == 3:
                rect[3] = rect[2] * (img_rect[3] / img_rect[2])
                rect[1] -= rect[3]/2
        
        return rect

    def update_hotkeys(self):
        for key in self.current_screen_data['hotkeys']:
            if self.keys[key]: 
                for command in self.current_screen_data['hotkeys'][key]: command[0](*command[1])

    def update_buttons(self):
        if not(self.mouse_buttons[0] and not self.mouse_states[0]): return
        for button in self.current_screen_data['buttons']:
            rect = self.get_rect(button)
            if not (rect[0] < self.mouse_pos[0] < rect[0] + rect[2] and rect[1] < self.mouse_pos[1] < rect[1] + rect[3]): continue
            button[2](*button[3])
            self.update_texture = 2

    def update_sliders(self):
        if not self.mouse_buttons[0]: return
        for slider in self.current_screen_data['sliders']:
            rect = self.get_rect(slider)
            if self.mouse_buttons[0]:
                if (rect[0] < self.mouse_pos[0] < rect[0] + rect[2] and rect[1] < self.mouse_pos[1] < rect[1] + rect[3]):
                    self.values[slider[3]] = min(max(((self.mouse_pos[0] - rect[0] + rect[3]/4) / rect[2]) * (slider[2][1] - slider[2][0]) + slider[2][0], slider[2][0]), slider[2][1])
                    self.values[slider[3]] -= self.values[slider[3]] % slider[2][2]
                    self.update_texture = 2

    def execute_draw_calls(self):
        for func in self.current_screen_data['draw_calls']:
            rect = self.get_rect([func[1][1]])
            func[0](self.surf, func[1][0], rect)

    def draw_sliders(self):
        for slider in self.current_screen_data['sliders']:
            rect = self.get_rect(slider)
            pg.draw.rect(self.surf, slider[1]/1.75, (rect[0], rect[1] + rect[3] / 4, rect[2], rect[3] / 2))
            pg.draw.rect(self.surf, (0, 0, 0), (rect[0], rect[1] + rect[3] / 4, rect[2], rect[3] / 2), 1)
            pg.draw.circle(self.surf, slider[1], (rect[0] + ((self.values[slider[3]] - slider[2][0]) / (slider[2][1] - slider[2][0])) * rect[2], rect[1] + rect[3] / 2), rect[3] / 2)
            pg.draw.circle(self.surf, (0, 0, 0), (rect[0] + ((self.values[slider[3]] - slider[2][0]) / (slider[2][1] - slider[2][0])) * rect[2], rect[1] + rect[3] / 2), rect[3] / 2, 1)

            self.text_handler.render_text(self.surf, (rect[0] + rect[2] + rect[3]/1.5, rect[1] - rect[3] * .15, rect[3] * 2, rect[3] * 1.3), f'{float(self.values[slider[3]]):.4}', 'default', 14, (255, 255, 255), (0, 0, 0, 100), True, True)

    def draw_text(self):
        for text_box in self.current_screen_data['text']:
            rect = self.get_rect(text_box)
            self.text_handler.render_text(self.surf, rect, *text_box[2])

    def draw_images(self):
        for button in self.current_screen_data['images']:
            rect = self.get_rect(button)
            img = pg.transform.scale(self.assets[button[1]], [*rect[2:]])
            self.surf.blit(img, rect)

    def main_menu(self):
        self.surf.fill((0, 0, 0, 100))
        self.draw()

    def pause(self):
        self.surf.fill((0, 0, 0, 100))
        self.draw()

    def settings_general(self):
        self.surf.fill((0, 0, 0, 100))
        self.draw()

    def settings_control(self):
        self.surf.fill((0, 0, 0, 100))
        self.draw()

    def settings_graphics(self):
        self.surf.fill((0, 0, 0, 100))
        self.draw()

    def hud(self):
        self.surf.fill((255, 0, 0, 0))
        self.draw()

        card_size = self.win_size[0] / self.n_cards / 2, self.win_size[1] / 5

        for i in range(self.n_cards):
            pg.draw.rect(self.surf, (255, 0, 0, 255), (self.win_size[0] / 2 - (card_size[0] + 5) * self.n_cards/2 + i * (card_size[0] + 5), self.win_size[1] - card_size[1] - 5, card_size[0], card_size[1]))