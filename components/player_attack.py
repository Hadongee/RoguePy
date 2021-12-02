from .component import Component
from .position import Position
from engine.actions import Action, AttackAction, AttackToggleAction
from entities.entity import Entity
from engine.gamestate import GameState

class PlayerAttack (Component):
    def __init__ (self, position : Position, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
        self.attack_confirm_function = None

    def handler_AttackAction (self, action : AttackAction):
        if self.attack_confirm_function != None:
            self.attack_confirm_function(self.position.x, self.position.y)

    def handler_AttackToggleAction (self, action : AttackToggleAction):
        self.attack_confirm_function = action.attack_confirm_function

    def bind (self):
        Action.add_action(AttackAction, self.handler_AttackAction)
        Action.add_action(AttackToggleAction, self.handler_AttackToggleAction)