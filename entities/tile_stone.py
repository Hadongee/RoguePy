from components.digable import Digable
from entities.entity_item import ItemEntity
from entities.tile_solid import SolidTile
from components.renderer import Renderer
from entities.tile_stone_floor import StoneFloorTile
from items.raw_stone import RawStoneItem

class StoneTile (SolidTile):
    def __init__ (self):
        super().__init__()
        self.description = "Stone Wall"
        self.get_component(Renderer).character="▓"
        self.get_component(Renderer).fg=[75, 75, 75]
        self.get_component(Digable).entities_dropped = [(StoneFloorTile(), 1), (ItemEntity(RawStoneItem()), 0.15)]