from items.equipment_slot import EquipmentSlot
from .equipment_item import EquipmentItem

class BasicPowerArmourBodyItem (EquipmentItem):
    def __init__ (self):
        super().__init__("Power Armour Body (Basic)", 1, [], EquipmentSlot.TORSO, fg=[32, 178, 170], character='¥')