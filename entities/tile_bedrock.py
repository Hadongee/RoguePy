from entities.tile_solid import SolidTile
from components.renderer import Renderer

class BedrockTile (SolidTile):
    def __init__ (self):
        super().__init__()
        self.get_component(Renderer).character="▓"
        self.get_component(Renderer).fg=[20, 20, 20]
        self.get_component(Renderer).always_visible = True
        self.get_component(Renderer).seen = True
        self.get_component(Renderer).visible = True