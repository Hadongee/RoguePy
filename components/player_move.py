from .component import Component
from .position import Position
from engine.actions import Action, MovementAction
from .solid import Solid

class PlayerMove (Component):
    def __init__ (self, position : Position or None = Position()):
        super().__init__()
        self.position = position

    def handler_MovementAction (self, action : MovementAction):
        if not Solid.is_solid(self.position.x + action.dx, self.position.y + action.dy):
            self.position.move(action.dx, action.dy)

    def bind (self):
        Action.add_action(MovementAction, self.handler_MovementAction)