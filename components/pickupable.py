from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState
from items.item import Item

class Pickupable (Component):
    def __init__ (self, item : Item or None = None, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.item = item
        
    def on_pickup (self) :
        pass