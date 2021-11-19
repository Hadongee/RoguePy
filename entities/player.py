from engine.gamestate import GameState
from .entity import Entity
from components.position import Position
from components.renderer import Renderer
from components.player_move import PlayerMove
from components.vision import Vision
from components.action_component_enabler import ActionComponentEnabler
from engine.actions import LookAction

class Player (Entity):
    def __init__ (self, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__()
        self.description = "Player"
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(Renderer(self.get_component(Position), character="@", fg=[0, 255, 255], always_visible=True))
        self.add_component(PlayerMove(self.get_component(Position)))
        self.add_component(Vision(self.get_component(Position)))
        self.add_component(ActionComponentEnabler([Vision], LookAction))