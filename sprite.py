# Contains basic structures for sprite entities

import numpy as np

class Sprite(object):
    
    def __init__(self, time):
        self.position = None
        self.skin = None
        self.dx = None
        self.dy = None
        self.last_update_time = time
    
    def update(self, time):
        net_time = time - self.last_update_time
        self.update_position(net_time)
        self.update_sprite(net_time)
        
        self.last_update_time = time
    
    def update_position(self, net_time):
        raise NotImplemented
    
    def update_sprite(self, net_time):
        raise NotImplemented
    
    
class Spark(Sprite):
    
    def __init__(self, position=(0,0), color=(255,0,0), dx=0, dy=0):
        self.position = position
        self.skin = [(0,0): color]]

    def update_position(net_time):
        x, y = self.position
        x += x + dx * net_time
        y += y + dy * net_time
        self.position = (x, y)
    
    def update_sprite(self, net_time)
        pass
    
