from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState

class Inventory (Component):
    def __init__ (self, max_slots : int, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.max_slots = max_slots
        self.items = list()
        
    def add_item (self, item):
        if len(self.items) < self.max_slots:
            # Add item
            self.items.append(item)
            return True
        else:
            return False