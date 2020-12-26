# Contains basic structures for sprite entities

import numpy as np

class Sprite(object):
    
    def __init__(self, time):
        self.position = None
        self.skin = None
        self.dx = None
        self.dy = None
        self.last_update_time = time
        self.live = True
    
    def update(self, time):
        net_time = time - self.last_update_time
        self.update_properties(net_time)
        self.update_position(net_time)
        self.update_skin(net_time)
        self.check_expire()
        
        self.last_update_time = time
    
    def update_properties(self, net_time):
        pass
    
    def update_position(self, net_time):
        raise NotImplemented
    
    def update_sprite(self, net_time):
        raise NotImplemented
    
    def check_expire(self):
        pass
    
class Spark(Sprite):
    skin_dim_x = 1
    skin_dim_y = 1
    
    def __init__(self, pos_x=0, pos_y=0, color=(255,0,0), dx=0, dy=1):
        self.position = position
        
        self.skin = np.zeros([skin_dim_y, skin_dim_x, 3], dtype=np.uint8)
        self.skin[0,0] = color

        self.dx = dx
        self.dy = dy
        
        self.live = True

    def update_position(net_time):
        self.pos_x += self.pos_x + self.dx * net_time
        self.pos_y += self.pos_y + self.dy * net_time
    
    def update_skin(self, net_time):
        pass
    
    def check_expire(self):
        if not 0 < self.pos_x <= 100 or not 0 < self.pos_y <= 100:
            self.live = False
        