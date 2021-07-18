from .entity import Entity
from components.position import Position
from components.renderer import Renderer
from components.player_move import PlayerMove

class Player (Entity):
    def __init__ (self, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__()
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(Renderer(character="@", fg=[0, 255, 255], position=self.get_component(Position)))
        self.add_component(PlayerMove(position=self.get_component(Position)))