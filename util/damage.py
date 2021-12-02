import random

class Damage ():
    def __init__ (self, min : int, max : int):
        self.min = min
        self.max = max
        
    def get_random (self):
        return random.randint(self.min, self.max)
    
    def get_min (self):
        return min
    
    def get_max (self):
        return max