# Contains objects and methods governing the overall behavior of the supporting framework

import numpy as np

RENDER_MODES = ('add', 'subtract', 'average')

class Controller(object):
    def __init__(self, display):
        self.display = display
        self.sprite_list= []
        

class Display(object):
    def __init__(self, dim_x, dim_y)
        self.dim_x = dim_x
        self.dim_y = dim_y
        self.display_data = self.blank()
    
    def blank(self):
        self.display_data = np.zeros([self.dim_y, self.dim_x, 3], dtype=np.uint8)
    
    def add_sprite(self, sprite, mode='add'):
        sprite_pos_x, sprite_pos_y = sprite.position
        sprite_dim_y, sprite_dim_x = sprite.skin.shape
        
        if mode == 'add':
            pass
        elif mode == 'subtract':
            pass
        elif mode == 'average':
            pass
    
    def show(self):
        raise NotImplemented

