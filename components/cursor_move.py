from .component import Component
from .position import Position
from engine.actions import Action, CursorMovementAction, DigMovementAction, DigToggleAction, LookToggleAction
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
            
    def handler_DigMovementAction (self, action : DigMovementAction):
        player_pos = self.game.player.get_component(Position)
        self.position.set(player_pos.x + action.dx, player_pos.y + action.dy)
        
    def handler_DigToggleAction (self, action : DigToggleAction):
        player_pos = self.game.player.get_component(Position)
        self.position.set(player_pos.x, player_pos.y)
    
    def handler_LookToggleAction (self, action : LookToggleAction):
        player_pos = self.game.player.get_component(Position)
        self.position.set(player_pos.x, player_pos.y)

    def bind (self):
        Action.add_action(CursorMovementAction, self.handler_CursorMovementAction)
        Action.add_action(DigMovementAction, self.handler_DigMovementAction)
        Action.add_action(DigToggleAction, self.handler_DigToggleAction)
        Action.add_action(LookToggleAction, self.handler_LookToggleAction)