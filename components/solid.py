from .component import Component
from .position import Position
from entities.entity import Entity
from engine.gamestate import GameState

class Solid (Component):
    solid_positions = list()

    def __init__ (self, position : Position, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position

    def bind (self):
        Solid.solid_positions.append(self.position)

    @classmethod
    def is_solid (cls, x : int, y : int):
        for solid in cls.solid_positions:
            if solid.x == x and solid.y == y:
                return True
        return False
