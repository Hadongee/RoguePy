from engine.actions import Action, DigAction
from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState

class PlayerStats (Component):
    def __init__ (self, max_health : int, max_energy : int, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.max_health = max_health
        self.health = max_health
        self.max_energy = max_energy
        self.energy = max_energy
        
    def change_energy (self, change : int):
        self.energy = self.energy + change
        if self.energy < 0:
            self.energy = 0
        if self.energy > self.max_energy:
            self.energy = self.max_energy