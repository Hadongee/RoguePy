from components.unmovable import Unmovable
from .component import Component
from .position import Position
from engine.actions import Action, MovementAction
from .solid import Solid
from entities.entity import Entity
from engine.gamestate import GameState

class PlayerMove (Component):
    def __init__ (self, position : Position, parent : Entity or None = None):
        super().__init__(parent, GameState.PLAYERTURN)
        self.position = position

    def handler_MovementAction (self, action : MovementAction):
        moving_to_solid = False
        for entity in Position.entities_at_position[self.position.x + action.dx, self.position.y + action.dy]:
            if entity.get_component(Solid) or entity.get_component(Unmovable):
                moving_to_solid = True
        if not moving_to_solid:
            self.position.move(action.dx, action.dy)

    def bind (self):
        Action.add_action(MovementAction, self.handler_MovementAction)