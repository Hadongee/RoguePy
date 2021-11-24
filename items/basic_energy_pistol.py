from items.equipment_slot import EquipmentSlot
from .equipment_item import EquipmentItem

class BasicEnergyPistolItem (EquipmentItem):
    def __init__ (self):
        super().__init__("Energy Pistol (Basic)", 1, [], EquipmentSlot.HANDS,fg=[0,255,255], character='⌐')