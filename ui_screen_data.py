import numpy as np
import pygame as pg

class ScreenData:
    def __init__(self, UI):
        self.screen_data = {
            UI.main_menu : {
                'images' : [

                ],
                'draw_calls' : [

                ],
                'text' : [
                    (np.array([.5, .2,  .6, .2]), None, ('Dicey Decks', 'default', 60, (220, 220, 220), (0, 0, 0, 100), True, True)),
                    (np.array([.5, .4,  .4, .1]), None, ('Start', 'default', 20, (220, 220, 220), (0, 0, 0, 100), True, True)),
                    (np.array([.5, .55, .4, .1]), None, ('Settings', 'default', 20, (220, 220, 220), (0, 0, 0, 100), True, True)),
                    (np.array([.5, .7,  .4, .1]), None, ('Quit', 'default', 20, (220, 220, 220), (0, 0, 0, 100), True, True))
                ],
                'buttons' : [
                    (np.array([.5, .4,  .6, .1]), None, UI.set_screen, [UI.hud]),
                    (np.array([.5, .55, .6, .1]), None, UI.set_screen, [UI.settings_general]),
                    (np.array([.5, .7,  .6, .1]), None, UI.log, ["quit"])
                ],
                'sliders' : [],
                'hotkeys' : {
                    pg.K_ESCAPE : [[UI.set_screen, [UI.hud]], [UI.log, ["Switching screen to HUD"]]],
                    pg.K_e : [[UI.log, ['Pressed "E"']]]
                }
            },

            UI.hud : {
                'images' : [

                ],
                'draw_calls' : [

                ],
                'text' : [
                    
                ],
                'buttons' : [
                    
                ],
                'sliders' : [
                    
                ],
                'hotkeys' : {
                    pg.K_ESCAPE : [[UI.set_screen, [UI.pause]]],
                    pg.K_e : [[UI.log, ['Pressed "E"']]]
                }
            },

            UI.pause : {
                'images' : [
                    
                ],
                'draw_calls' : [],
                'text' : [
                    (np.array([.5, .4,  .6, .1]), None, ('Resume', 'default', 20, (220, 220, 220), (0, 0, 0, 100), True, True)),
                    (np.array([.5, .55, .6, .1]), None, ('Settings', 'default', 20, (220, 220, 220), (0, 0, 0, 100), True, True)),
                    (np.array([.5, .7,  .6, .1]), None, ('Exit', 'default', 20, (220, 220, 220), (0, 0, 0, 100), True, True))
                ],
                'buttons' : [
                    (np.array([.5, .4,  .6, .1]), None, UI.set_screen, [UI.hud]),
                    (np.array([.5, .55, .6, .1]), None, UI.set_screen, [UI.settings_general]),
                    (np.array([.5, .7,  .6, .1]), None, UI.set_screen, [UI.main_menu])
                ],
                'sliders' : [],
                'hotkeys' : {
                    pg.K_ESCAPE : [[UI.set_screen, [UI.hud]]]
                }
            },

            UI.settings_general : {
                'images' : [

                ],
                'draw_calls' : [
                    (pg.draw.rect, [(0, 0, 0, 200), np.array([0.3, 0.5, 0.005, 0.8])])
                ],
                'text' : [
                    (np.array([.15, .2,  .275, .1]),    None, ('General', 'default', 20, (220, 220, 220), (200, 200, 200, 100), True, True)),
                    (np.array([.15, .32,  .275, .1]),   None, ('Controls', 'default', 20, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.15, .44,  .275, .1]),   None, ('Graphics', 'default', 20, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.15, .86,  .275, .075]), None, ('Back', 'default', 16, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.9, .86,  .175, .075]),  None, ('Apply', 'default', 16, (120, 120, 120), (0, 0, 0, 100), True, True)),

                    (np.array([.425, .175, .2, .05]),    None, ('Volume', 'default', 16, (220, 220, 220), (0, 0, 0, 100), True, True)),
                ],
                'buttons' : [
                    (np.array([.15, .2,  .275, .1]),    None, UI.set_screen, [UI.settings_general]),
                    (np.array([.15, .32,  .275, .1]),   None, UI.set_screen, [UI.settings_control]),
                    (np.array([.15, .44,  .275, .1]),   None, UI.set_screen, [UI.settings_graphics]),
                    (np.array([.15, .86,  .275, .075]), None, UI.set_screen, [UI.pause]),
                    (np.array([.9, .86,  .175, .075]),  None, UI.log, ['Apply Settings'])
                ],
                'sliders' : [
                    (np.array([.75, .175, .3, .05]), np.array([50, 150, 255]), (0, 100, 1), 'volume')
                ],
                'hotkeys' : {
                    pg.K_ESCAPE : [[UI.set_screen, [UI.pause]]]
                }
            },

            UI.settings_control : {
                'images' : [

                ],
                'draw_calls' : [
                    (pg.draw.rect, [(0, 0, 0, 200), np.array([0.3, 0.5, 0.005, 0.8])])
                ],
                'text' : [
                    (np.array([.15, .2,  .275, .1]),    None, ('General', 'default', 20, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.15, .32,  .275, .1]),   None, ('Controls', 'default', 20, (220, 220, 220), (200, 200, 200, 100), True, True)),
                    (np.array([.15, .44,  .275, .1]),   None, ('Graphics', 'default', 20, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.15, .86,  .275, .075]), None, ('Back', 'default', 16, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.9, .86,  .175, .075]),  None, ('Apply', 'default', 16, (120, 120, 120), (0, 0, 0, 100), True, True)),
                ],
                'buttons' : [
                    (np.array([.15, .2,  .275, .1]),    None, UI.set_screen, [UI.settings_general]),
                    (np.array([.15, .32,  .275, .1]),   None, UI.set_screen, [UI.settings_control]),
                    (np.array([.15, .44,  .275, .1]),   None, UI.set_screen, [UI.settings_graphics]),
                    (np.array([.15, .86,  .275, .075]), None, UI.set_screen, [UI.pause]),
                    (np.array([.9, .86,  .175, .075]),  None, UI.log, ['Apply Settings'])
                ],
                'sliders' : [],
                'hotkeys' : {
                    pg.K_ESCAPE : [[UI.set_screen, [UI.pause]]]
                }
            },

            UI.settings_graphics : {
                'images' : [

                ],
                'draw_calls' : [
                    (pg.draw.rect, [(0, 0, 0, 200), np.array([0.3, 0.5, 0.005, 0.8])])
                ],
                'text' : [
                    (np.array([.15, .2,  .275, .1]),    None, ('General', 'default', 20, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.15, .32,  .275, .1]),   None, ('Controls', 'default', 20, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.15, .44,  .275, .1]),   None, ('Graphics', 'default', 20, (220, 220, 220), (200, 200, 200, 100), True, True)),
                    (np.array([.15, .86,  .275, .075]), None, ('Back', 'default', 16, (120, 120, 120), (0, 0, 0, 100), True, True)),
                    (np.array([.9, .86,  .175, .075]),  None, ('Apply', 'default', 16, (120, 120, 120), (0, 0, 0, 100), True, True)),

                    (np.array([.425, .175, .2, .05]),   None, ('FOV', 'default', 16, (220, 220, 220), (0, 0, 0, 100), True, True)),
                    (np.array([.425, .25, .2, .05]),   None, ('Chunk Distance', 'default', 16, (220, 220, 220), (0, 0, 0, 100), True, True)),
                    (np.array([.425, .325, .2, .05]),   None, ('View Distance', 'default', 16, (220, 220, 220), (0, 0, 0, 100), True, True)),
                    (np.array([.425, .4, .2, .05]),   None, ('Light Distance', 'default', 16, (220, 220, 220), (0, 0, 0, 100), True, True)),
                ],
                'buttons' : [
                    (np.array([.15, .2,  .275, .1]),    None, UI.set_screen, [UI.settings_general]),
                    (np.array([.15, .32,  .275, .1]),   None, UI.set_screen, [UI.settings_control]),
                    (np.array([.15, .44,  .275, .1]),   None, UI.set_screen, [UI.settings_graphics]),
                    (np.array([.15, .86,  .275, .075]), None, UI.set_screen, [UI.pause]),
                    (np.array([.9, .86,  .175, .075]),  None, UI.log, ['Apply Settings']),
                ],
                'sliders' : [
                    (np.array([.75, .175, .3, .05]), np.array([50, 150, 255]), (50, 120, 1), 'FOV'),
                    (np.array([.75, .25, .3, .05]), np.array([50, 150, 255]), (3, 20, 1), 'render_distance'),
                    (np.array([.75, .325, .3, .05]), np.array([50, 150, 255]), (100, 400, 10), 'view_distance'),
                    (np.array([.75, .4, .3, .05]), np.array([50, 150, 255]), (10, 100, 5), 'lighting_distance')
                ],
                'hotkeys' : {
                    pg.K_ESCAPE : [[UI.set_screen, [UI.pause]]]
                }
            },

        }