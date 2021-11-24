from items.equipment_slot import EquipmentSlot
from .equipment_item import EquipmentItem

class BasicPowerArmourHelmetItem (EquipmentItem):
    def __init__ (self):
        super().__init__("Power Armour Helmet (Basic)", 1, [], EquipmentSlot.HEAD, fg=[32, 178, 170], character='ô')