from entities.tile import Tile
from components.position import Position
from components.renderer import Renderer
from components.solid import Solid

import random

class GrassTile (Tile):
    def __init__ (self):
        super().__init__()
        self.add_component(Position(0, 0))
        self.add_component(Renderer(self.get_component(Position), character=" "))
    
    def on_created (self):
        floor_characters = [' ', '.', ',', '\'', '"', '`']
        random_color = [[50,205,50], [154,205,50], [0,100,0], [107,142,35]]
        renderer = self.get_component(Renderer)
        renderer.character = random.choice(floor_characters)
        renderer.fg = random.choice(random_color)