from entities.tile import Tile
from components.position import Position
from components.renderer import Renderer
from components.solid import Solid

class SolidTile (Tile):
    def __init__ (self):
        super().__init__()
        self.add_component(Position(0, 0))
        self.add_component(Renderer(character=" ", bg=[50, 50, 50], position=self.get_component(Position)))
        self.add_component(Solid(self.get_component(Position)))