from components.inventory import Inventory
from components.position import Position
from components.player_stats import PlayerStats

from entities.entity_item import ItemEntity

class ItemAction ():
    def __init__ (self, name : str):
        self.name = name
    
    def on_use (self, inventory_slot, game):
        pass
    
    def delete_from_inventory (self, amount, inventory_slot, inventory):
        if inventory_slot['stack_size'] >= amount:
            inventory_slot['stack_size'] -= amount
            
            if inventory_slot['stack_size'] == 0:
                inventory.items.remove(inventory_slot)
            return True
        else:
            return False
    
class DropItemAction (ItemAction):
    def __init__ (self):
        super().__init__("Drop")
        
    def on_use(self, inventory_slot, game):
        super().on_use(inventory_slot, game)
        if self.delete_from_inventory(1, inventory_slot, game.player.get_component(Inventory)):
            game.add_entity(ItemEntity(inventory_slot['item'], game.player.get_component(Position).x, game.player.get_component(Position).y))
        
class PowerUpItemAction (ItemAction):
    def __init__(self, power):
        super().__init__("Power Up")
        self.power = power
        
    def on_use (self, inventory_slot, game):
        super().on_use(inventory_slot, game)
        if self.delete_from_inventory(1, inventory_slot, game.player.get_component(Inventory)):
            game.player.get_component(PlayerStats).change_energy(self.power)