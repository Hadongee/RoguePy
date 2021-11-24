import random

class Damage ():
    def __init__ (self, min : int, max : int):
        self.min = min
        self.max = max
        
    def get_random (self):
        return random.randint(min, max)
    
    def get_min (self):
        return min
    
    def get_max (self):
        return max