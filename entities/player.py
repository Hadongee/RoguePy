from components.inventory import Inventory
from components.player_stats import PlayerStats
from engine.gamestate import GameState
from .entity import Entity
from components.position import Position
from components.renderer import Renderer
from components.player_move import PlayerMove
from components.vision import Vision
from components.action_component_enabler import ActionComponentEnabler
from engine.actions import DigToggleAction, LookToggleAction, DigAction, PickupToggleAction, PickupAction
from engine.settings_handler import SettingsHandler

class Player (Entity):
    def __init__ (self, game, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__()
        self.description = "Player"
        settings = SettingsHandler().settings
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(Renderer(self.get_component(Position), character="@", fg=[0, 255, 255], always_visible=True, render_on_late_update=True))
        self.add_component(PlayerMove(self.get_component(Position)))
        self.add_component(Vision(self.get_component(Position)))
        self.add_component(PlayerStats(settings.max_health, settings.max_energy))
        self.add_component(ActionComponentEnabler([Vision], LookToggleAction))
        self.add_component(ActionComponentEnabler([Vision], DigToggleAction))
        self.add_component(ActionComponentEnabler([Vision], DigAction))
        self.add_component(ActionComponentEnabler([Vision], PickupToggleAction))
        self.add_component(ActionComponentEnabler([Vision], PickupAction))
        self.add_component(Inventory(24))