from typing import Tuple


class SingleAnimation ():
    def __init__ (self, position : Tuple, character : chr, fg : list):
        self.position = position
        self.character = character
        self.fg = fg

class Animation ():
    animations = list()
    
    @classmethod
    def add_animation (cls, anim : SingleAnimation):
        cls.animations.append(anim)
        
    @classmethod
    def clear_animation (cls):
        cls.animations.clear()