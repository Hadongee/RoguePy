from entities.tile_solid import SolidTile
from components.renderer import Renderer
from components.digable import Digable

class BedrockTile (SolidTile):
    def __init__ (self):
        super().__init__()
        self.description = "Bedrock"
        self.get_component(Renderer).character="#"
        self.get_component(Renderer).fg=[35, 35, 35]
        self.get_component(Renderer).always_visible = True
        self.get_component(Renderer).seen = True
        self.get_component(Renderer).visible = True
        self.del_component(self.get_component(Digable))