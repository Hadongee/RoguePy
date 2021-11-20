from components.player_stats import PlayerStats
from .component import Component
from .position import Position
from engine.actions import Action, MovementAction
from .solid import Solid
from entities.entity import Entity
from engine.gamestate import GameState

class PlayerMove (Component):
    def __init__ (self, position : Position, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
        self.energy_for_move = 1

    def handler_MovementAction (self, action : MovementAction):
        if self.entity.get_component(PlayerStats).energy >= self.energy_for_move:
            moving_to_solid = False
            for entity in Position.entities_at_position[self.position.x + action.dx, self.position.y + action.dy]:
                if entity.get_component(Solid):
                    moving_to_solid = True
            if not moving_to_solid:
                self.position.move(action.dx, action.dy)
                self.entity.get_component(PlayerStats).change_energy(-self.energy_for_move)

    def bind (self):
        Action.add_action(MovementAction, self.handler_MovementAction)