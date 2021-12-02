from components.enemy_controller import EnemyController
from components.health import Health
from components.position import Position
from engine.actions import AttackToggleAction
from engine.input_handlers import EventHandlerState
from items.equipment_slot import EquipmentSlot
from .equipment_item import EquipmentItem
from util.damage import Damage

class BasicEnergyPistolItem (EquipmentItem):
    def __init__ (self):
        super().__init__("Energy Pistol (Basic)", 1, [], EquipmentSlot.HANDS, use_action=AttackToggleAction(self.attack_confirm), event_handler_state=EventHandlerState.ATTACK, fg=[0,255,255], character='⌐')
        self.damage = Damage(5, 8)
        
    def attack_confirm (self, pos_x : int, pos_y : int):
        for entity in Position.entities_at_position[(pos_x, pos_y)]:
            if entity.get_component(EnemyController) != None:
                entity.get_component(Health).deal_damage(self.damage.get_random())