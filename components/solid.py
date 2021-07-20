from .component import Component
from .position import Position

class Solid (Component):
    solid_positions = list()

    def __init__ (self, position : Position):
        super().__init__()
        self.position = position

    def bind (self):
        Solid.solid_positions.append(self.position)

    @classmethod
    def is_solid (cls, x : int, y : int):
        for solid in cls.solid_positions:
            if solid.x == x and solid.y == y:
                return True
        return False