from components.player_stats import PlayerStats
from entities.player import Player
from .component import Component
from .position import Position
from engine.actions import Action, DigAction
from .digable import Digable
from entities.entity import Entity
from engine.gamestate import GameState

class Dig (Component):
    def __init__ (self, position : Position, game, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
        self.game = game
        self.energy_for_dig = 3

    def handler_DigAction (self, action : DigAction):
        if self.game.player.get_component(PlayerStats).energy >= self.energy_for_dig:
            dig_x = self.position.x
            dig_y = self.position.y
            
            if (dig_x, dig_y) in Position.entities_at_position and len(Position.entities_at_position[(dig_x, dig_y)]) > 0:
                for entity in Position.entities_at_position[(dig_x, dig_y)]:
                    if entity != self.entity and entity.get_component(Digable) != None:
                        entity.get_component(Digable).on_dig(self.game)
                        self.game.player.get_component(PlayerStats).change_energy(-self.energy_for_dig)

    def bind (self):
        Action.add_action(DigAction, self.handler_DigAction)