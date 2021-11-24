from items.equipment_slot import EquipmentSlot
from .equipment_item import EquipmentItem

class BasicPowerArmourFeetItem (EquipmentItem):
    def __init__ (self):
        super().__init__("Power Armour Boots (Basic)", 1, [], EquipmentSlot.FEET, fg=[32, 178, 170], character='∞')