from .tile import Tile
from components.renderer import Renderer
from components.position import Position
import random

class StoneFloorTile (Tile):
    def __init__ (self):
        super().__init__()
        self.description = "Stone Floor"
        self.add_component(Renderer(self.get_component(Position), character=".", fg=[75, 75, 75]))
        
    def on_created (self):
        floor_characters = ['.', ',', '`']
        renderer = self.get_component(Renderer)
        renderer.character = random.choice(floor_characters)
        renderer.fg = [75, 75, 75]