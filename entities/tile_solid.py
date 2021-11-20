from entities.tile import Tile
from components.position import Position
from components.renderer import Renderer
from components.solid import Solid
from components.digable import Digable

class SolidTile (Tile):
    def __init__ (self):
        super().__init__()
        self.add_component(Renderer(self.get_component(Position), character="▓", fg=[255,0,255]))
        self.add_component(Solid(self.get_component(Position)))
        self.add_component(Digable(self.get_component(Position)))