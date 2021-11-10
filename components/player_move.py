from .component import Component
from .position import Position
from engine.actions import Action, MovementAction
from .solid import Solid
from entities.entity import Entity

class PlayerMove (Component):
    def __init__ (self, parent : Entity, position : Position):
        super().__init__(parent)
        self.position = position

    def handler_MovementAction (self, action : MovementAction):
        if not Solid.is_solid(self.position.x + action.dx, self.position.y + action.dy):
            self.position.move(action.dx, action.dy)

    def bind (self):
        Action.add_action(MovementAction, self.handler_MovementAction)