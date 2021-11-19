from .component import Component
from .position import Position
from engine.actions import Action, CursorMovementAction
from entities.entity import Entity
from engine.gamestate import GameState

class CursorMove (Component):
    def __init__ (self, position : Position, game_width : int, game_height : int, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
        self.game_width = game_width
        self.game_height = game_height

    def handler_CursorMovementAction (self, action : CursorMovementAction):
        if self.position.x + action.dx >= 0 and self.position.x + action.dx < self.game_width and self.position.y + action.dy >= 0 and self.position.y + action.dy < self.game_height:
            self.position.move(action.dx, action.dy)

    def bind (self):
        Action.add_action(CursorMovementAction, self.handler_CursorMovementAction)