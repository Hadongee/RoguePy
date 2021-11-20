from components.digable import Digable
from entities.item_gold import GoldItemEntity
from .tile_solid import SolidTile
from components.renderer import Renderer
from .tile_stone_floor import StoneFloorTile

class GoldTile (SolidTile):
    def __init__ (self):
        super().__init__()
        self.description = "Gold Vein"
        self.get_component(Renderer).character="░"
        self.get_component(Renderer).fg=[255, 255, 0]
        self.get_component(Digable).entities_dropped = [StoneFloorTile(), GoldItemEntity()]