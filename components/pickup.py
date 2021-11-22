from components.inventory import Inventory
from components.pickupable import Pickupable
from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState
from .position import Position
from engine.actions import Action, PickupAction

class Pickup (Component):
    def __init__ (self, position : Position, inventory : Inventory, game, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
        self.game = game
        self.inventory = inventory
        
    def handler_PickupAction (self, action : PickupAction):
        pickup_x = self.position.x
        pickup_y = self.position.y
        
        if (pickup_x, pickup_y) in Position.entities_at_position and len(Position.entities_at_position[(pickup_x, pickup_y)]) > 0:
                for entity in Position.entities_at_position[(pickup_x, pickup_y)]:
                    if entity != self.entity and entity.get_component(Pickupable) != None:
                        entity.get_component(Pickupable).on_pickup()
                        self.inventory.add_item(entity.get_component(Pickupable).item)
                        self.game.del_entity(entity)
                        print(self.inventory.items)
                        break

    def bind (self):
        Action.add_action(PickupAction, self.handler_PickupAction)