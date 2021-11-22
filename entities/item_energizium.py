from .entity_item import ItemEntity
from components.renderer import Renderer
from items.item_energizium import EnergiziumItem

class EnergiziumItemEntity (ItemEntity):
    def __init__ (self, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__(EnergiziumItem("Energizium"), spawn_x, spawn_y)
        self.description="Raw Energizium Ore"
        self.get_component(Renderer).character="&"
        self.get_component(Renderer).fg=[255, 0, 255]