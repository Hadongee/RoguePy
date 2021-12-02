from components.inventory import Inventory
from components.player_attack import PlayerAttack
from entities.entity import Entity
from components.position import Position
from components.cursor_renderer import CursorRenderer
from components.action_component_enabler import ActionComponentEnabler
from components.cursor_move import CursorMove
from components.cursor_look import CursorLook
from components.pickup import Pickup
from components.dig import Dig
from engine.actions import AttackAction, AttackToggleAction, DigAction, LookToggleAction, DigToggleAction, PickupAction, PickupToggleAction

class Cursor (Entity):
    def __init__ (self, game, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__()
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(CursorRenderer(self.get_component(Position)))
        self.get_component(CursorRenderer).enabled = False
        self.add_component(CursorLook(self.get_component(Position)))
        self.get_component(CursorLook).enabled = False
        self.add_component(PlayerAttack(self.get_component(Position)))
        self.add_component(ActionComponentEnabler([CursorRenderer, CursorLook], LookToggleAction))
        self.add_component(ActionComponentEnabler([CursorRenderer], DigToggleAction))
        self.add_component(ActionComponentEnabler([CursorRenderer], DigAction))
        self.add_component(ActionComponentEnabler([CursorRenderer], PickupAction))
        self.add_component(ActionComponentEnabler([CursorRenderer], PickupToggleAction))
        self.add_component(ActionComponentEnabler([CursorRenderer], AttackAction))
        self.add_component(ActionComponentEnabler([CursorRenderer], AttackToggleAction))
        self.add_component(CursorMove(self.get_component(Position), game))
        self.add_component(Dig(self.get_component(Position), game))
        self.add_component(Pickup(self.get_component(Position), game.player.get_component(Inventory), game))