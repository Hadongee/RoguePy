from entities.tile_solid import SolidTile
from components.renderer import Renderer

class StoneTile (SolidTile):
    def __init__ (self):
        super().__init__()
        self.description = "Stone"
        self.get_component(Renderer).character="▓"
        self.get_component(Renderer).fg=[75, 75, 75]