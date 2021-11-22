from components.pickupable import Pickupable
from .entity import Entity
from components.position import Position
from components.renderer import Renderer
from items.item import Item

class ItemEntity (Entity):
    def __init__ (self, item : Item or None = None, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__(description="Entity Item")
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(Renderer(self.get_component(Position), character="o", fg=[255, 255, 255]))
        self.add_component(Pickupable(item))