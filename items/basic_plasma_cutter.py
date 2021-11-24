from components.equipment import EquipmentSlot
from engine.input_handlers import EventHandlerState
from items.equipment_item import EquipmentItem
from .equipment_item import EquipmentItem
from engine.actions import DigToggleAction

class BasicPlasmaCutterItem (EquipmentItem):
    def __init__ (self):
        super().__init__("Plasma Cutter (Basic)", 1, [], EquipmentSlot.HANDS, use_action=DigToggleAction(), event_handler_state=EventHandlerState.DIG, fg=[255, 102, 178], character='û')