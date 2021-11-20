from .entity import Entity
from components.position import Position
from components.renderer import Renderer

class GoldItemEntity (Entity):
    def __init__ (self, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__(description="A pile of gold nuggets")
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(Renderer(self.get_component(Position), character="$", fg=[255, 255, 0]))