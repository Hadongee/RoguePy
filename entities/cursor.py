from entities.entity import Entity
from components.position import Position
from components.renderer import Renderer
from components.action_component_enabler import ActionComponentEnabler
from components.cursor_move import CursorMove
from components.cursor_look import CursorLook
from engine.actions import LookToggleAction

class Cursor (Entity):
    def __init__ (self, game_width : int, game_height : int, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__()
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(Renderer(self.get_component(Position), character="X", fg=[0, 255, 255], always_visible=True, render_on_late_update=True))
        self.get_component(Renderer).enabled = False
        self.add_component(CursorLook(self.get_component(Position)))
        self.get_component(CursorLook).enabled = False
        self.add_component(ActionComponentEnabler([Renderer, CursorLook], LookToggleAction))
        self.add_component(CursorMove(self.get_component(Position), game_width, game_height))