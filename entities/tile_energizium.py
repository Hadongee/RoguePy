from components.digable import Digable
from entities.item_energizium import EnergiziumItemEntity
from .tile_solid import SolidTile
from components.renderer import Renderer
from .tile_stone_floor import StoneFloorTile

class EnergiziumTile (SolidTile):
    def __init__ (self):
        super().__init__()
        self.description = "Energizium Vein"
        self.get_component(Renderer).character="░"
        self.get_component(Renderer).fg=[255, 0, 255]
        self.get_component(Digable).entities_dropped = [StoneFloorTile(), EnergiziumItemEntity()]