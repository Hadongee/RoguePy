from entities.tile import Tile
from components.position import Position
from components.renderer import Renderer
from components.solid import Solid

import random

class GrassTile (Tile):
    def __init__ (self):
        super().__init__()
        self.description = "Grass"
        self.add_component(Renderer(self.get_component(Position), character=" "))
    
    def on_created (self):
        floor_characters = ['.', ',', '\'', '"', '`']
        random_color = [[50,205,50], [154,205,50], [0,100,0], [107,142,35]]
        renderer = self.get_component(Renderer)
        renderer.character = random.choice(floor_characters)
        if renderer.character == '"':
            self.description = "Dense grass"
        else:
            self.description = "Short grass"
        renderer.fg = random.choice(random_color)