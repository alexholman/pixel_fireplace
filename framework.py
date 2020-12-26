# Contains objects and methods governing the overall behavior of the supporting framework

import numpy as np

RENDER_MODES = ('add', 'subtract', 'overlay', 'average')

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
        sprite_dim_y, sprite_dim_x = sprite.skin.shape
        sprite_pos_x_end = sprite.pos_x + sprite_dim_x
        sprite_pos_y_end = sprite.pos_y + sprite_dim_y
        
        
        if mode == 'add':
            self.display_data[sprite.pos_y:sprite_pos_y_end, spite.pos_x:sprite_pos_x_end] += sprite.skin
        elif mode == 'subtract':
            self.display_data[sprite.pos_y:sprite_pos_y_end, spite.pos_x:sprite_pos_x_end] -= sprite.skin
        elif mode == 'overlay':
            self.display_data[sprite.pos_y:sprite_pos_y_end, spite.pos_x:sprite_pos_x_end] = sprite.skin
        elif mode == 'average':
            pass

    def show(self):
        raise NotImplemented

