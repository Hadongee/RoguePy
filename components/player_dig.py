from .component import Component
from .position import Position
from engine.actions import Action, DigAction
from .solid import Solid
from entities.entity import Entity
from engine.gamestate import GameState

class PlayerDig (Component):
    def __init__ (self, position : Position, game, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
        self.game = game

    def handler_DigAction (self, action : DigAction):
        dig_x = self.position.x + action.dx
        dig_y = self.position.y + action.dy
        
        if (dig_x, dig_y) in Position.entities_at_position and len(Position.entities_at_position[(dig_x, dig_y)]) > 0:
            for entity in Position.entities_at_position[(dig_x, dig_y)]:
                if entity.diggable:
                    self.game.entities.remove(entity)
                    Position.entities_at_position[(dig_x, dig_y)].remove(entity)

    def bind (self):
        Action.add_action(DigAction, self.handler_DigAction)