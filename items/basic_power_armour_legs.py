from items.equipment_slot import EquipmentSlot
from .equipment_item import EquipmentItem

class BasicPowerArmourLegsItem (EquipmentItem):
    def __init__ (self):
        super().__init__("Power Armour Legs (Basic)", 1, [], EquipmentSlot.LEGS, fg=[32, 178, 170], character='∩')