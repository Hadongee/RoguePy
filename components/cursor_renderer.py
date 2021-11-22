from components.digable import Digable
from components.pickupable import Pickupable
from components.player_stats import PlayerStats
from .renderer import Renderer
from .position import Position
from engine.actions import Action, DigToggleAction, DigAction, LookToggleAction, PickupAction, PickupToggleAction

class CursorRenderer (Renderer):
    def __init__ (self, position : Position):
        super().__init__(position, character="X", fg=[0, 255, 255], always_visible=True, render_on_late_update=True)
        self.default_fg = [0, 255, 255]
        self.valid_fg = [0, 255, 0]
        self.invalid_fg = [255, 0, 0]
        self.mining = False
        self.pickup = False
    
    def update (self, game):
        super().update(game)
        if self.mining:
            if game.player.get_component(PlayerStats).energy > 0:
                for entity in Position.entities_at_position[(self.position.x, self.position.y)]:
                    if entity.get_component(Digable) != None:
                        self.fg = self.valid_fg
                        break
                else:
                    self.fg = self.invalid_fg
            else:
                self.fg = self.invalid_fg
        if self.pickup:
            for entity in Position.entities_at_position[(self.position.x, self.position.y)]:
                if entity.get_component(Pickupable) != None:
                    self.fg = self.valid_fg
                    break
            else:
                self.fg = self.invalid_fg
        
    def handler_DigToggleAction (self, action):
        self.mining = not self.mining
        
    def handler_PickupToggleAction (self, action):
        self.pickup = not self.pickup
    
    def handler_LookToggleAction (self, action : LookToggleAction):
        self.fg = self.default_fg

    def bind (self):
        Action.add_action(DigToggleAction, self.handler_DigToggleAction)
        Action.add_action(DigAction, self.handler_DigToggleAction)
        Action.add_action(PickupToggleAction, self.handler_PickupToggleAction)
        Action.add_action(PickupAction, self.handler_PickupToggleAction)
        Action.add_action(LookToggleAction, self.handler_LookToggleAction)