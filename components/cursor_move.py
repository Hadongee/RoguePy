from .component import Component
from .position import Position
from engine.actions import Action, AttackToggleAction, PickupToggleAction, CursorMovementAction, DigMovementAction, DigToggleAction, LookToggleAction, PickupMovementAction
from entities.entity import Entity
from engine.gamestate import GameState

class CursorMove (Component):
    def __init__ (self, position : Position, game, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
        self.game = game

    def handler_CursorMovementAction (self, action : CursorMovementAction):
        if self.position.x + action.dx >= 0 and self.position.x + action.dx < self.game.game_width and self.position.y + action.dy >= 0 and self.position.y + action.dy < self.game.game_height:
            self.position.move(action.dx, action.dy)
            
    def handler_AdjacentMovementAction (self, action):
        player_pos = self.game.player.get_component(Position)
        self.position.set(player_pos.x + action.dx, player_pos.y + action.dy)
        
    def handler_ResetPosition (self, action):
        player_pos = self.game.player.get_component(Position)
        self.position.set(player_pos.x, player_pos.y)

    def bind (self):
        Action.add_action(CursorMovementAction, self.handler_CursorMovementAction)
        Action.add_action(DigMovementAction, self.handler_AdjacentMovementAction)
        Action.add_action(PickupMovementAction, self.handler_AdjacentMovementAction)
        Action.add_action(DigToggleAction, self.handler_ResetPosition)
        Action.add_action(AttackToggleAction, self.handler_ResetPosition)
        Action.add_action(LookToggleAction, self.handler_ResetPosition)
        Action.add_action(PickupToggleAction, self.handler_ResetPosition)