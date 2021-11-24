from components.pickupable import Pickupable
from .entity import Entity
from components.position import Position
from components.renderer import Renderer
from items.item import Item

class DropPod (Entity):
    def __init__ (self, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__(description="Drop Pod")
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(Renderer(self.get_component(Position), character="Ä", fg=[255, 255, 255]))