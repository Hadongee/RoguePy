from engine.actions import Action
from engine.input_handlers import EventHandlerState
from .item import Item
from items.equipment_slot import EquipmentSlot
from .item_actions import EquipItemAction, UnequipItemAction

class EquipmentItem (Item) :
    def __init__ (self, name : str, maximum_stack : int, item_actions: list, equipment_slot : EquipmentSlot, use_action : Action or None = None, event_handler_state : EventHandlerState or None = None, fg : list or None = [255, 255, 255], bg : list or None = [0, 0, 0], character : str or None = "o"):
        if equipment_slot == EquipmentSlot.HANDS:
            item_actions.append(EquipItemAction(EquipmentSlot.LEFT_HAND))
            item_actions.append(EquipItemAction(EquipmentSlot.RIGHT_HAND))
        else:
            item_actions.append(EquipItemAction(equipment_slot))
        item_actions.append(UnequipItemAction())
        super().__init__(name, maximum_stack, item_actions, fg, bg, character)
        self.equipment_slot = equipment_slot
        self.equipped = None
        self.use_action = use_action
        self.event_handler_state = event_handler_state