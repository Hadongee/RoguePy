from .entity_item import ItemEntity
from components.position import Position
from components.renderer import Renderer

class GoldItemEntity (ItemEntity):
    def __init__ (self, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__(spawn_x, spawn_y)
        self.description="A pile of gold nuggets"
        self.get_component(Renderer).character="$"
        self.get_component(Renderer).fg=[255, 255, 0]