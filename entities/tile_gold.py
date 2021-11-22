from components.digable import Digable
from entities.entity_item import ItemEntity
from .tile_solid import SolidTile
from components.renderer import Renderer
from .tile_stone_floor import StoneFloorTile
from items.raw_gold import RawGoldItem

class GoldTile (SolidTile):
    def __init__ (self):
        super().__init__()
        self.description = "Gold Vein"
        self.get_component(Renderer).character="░"
        self.get_component(Renderer).fg=[255, 255, 0]
        self.get_component(Digable).entities_dropped = [(StoneFloorTile(), 1), (ItemEntity(RawGoldItem()), 1)]