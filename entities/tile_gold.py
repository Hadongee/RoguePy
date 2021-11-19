from entities.tile_solid import SolidTile
from components.renderer import Renderer

class GoldTile (SolidTile):
    def __init__ (self):
        super().__init__()
        self.description = "Gold"
        self.get_component(Renderer).character="░"
        self.get_component(Renderer).fg=[255, 255, 0]