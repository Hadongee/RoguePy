from .item import Item
from .item_actions import DropItemAction, PowerUpItemAction

class RawEnergiziumItem (Item):
    def __init__ (self):
        super().__init__("Raw Energizium Ore", 10, [PowerUpItemAction(100), DropItemAction()], fg=[255, 0, 255], character='&')