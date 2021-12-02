from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState

class Unmovable (Component):
    def __init__ (self, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)