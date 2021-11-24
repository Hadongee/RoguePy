from engine.gamestate import GameState
from entities.entity import Entity
from .component import Component
from items.equipment_slot import EquipmentSlot

class Equipment (Component):
    def __init__ (self, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.slots = dict()
        for slot in EquipmentSlot:
            if slot.value != 0:
                self.slots[slot.name] = None
    
    def equip_item (self, item, equip_slot : EquipmentSlot):
        if self.slots[equip_slot.name] != None:
            self.slots[equip_slot.name].equipped = None
        if equip_slot == EquipmentSlot.LEFT_HAND and self.slots[EquipmentSlot.RIGHT_HAND.name] == item:
            self.slots[EquipmentSlot.RIGHT_HAND.name].equipped = None
        elif equip_slot == EquipmentSlot.RIGHT_HAND and self.slots[EquipmentSlot.LEFT_HAND.name] == item:
            self.slots[EquipmentSlot.LEFT_HAND.name].equipped = None
        item.equipped = equip_slot
        self.slots[equip_slot.name] = item
    
    def unequip_item (self, equip_slot : EquipmentSlot):
        self.slots[equip_slot.name].equipped = None
        self.slots[equip_slot.name] = None