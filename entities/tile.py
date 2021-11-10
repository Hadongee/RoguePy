from entities.entity import Entity
from components.position import Position

class Tile (Entity):
    def __init__ (self):
        super().__init__()
        self.add_component(Position(self, 0, 0))