from .item import Item
from .item_actions import DropItemAction, PowerUpItemAction

class RawEnergiziumItem (Item):
    def __init__ (self):
        super().__init__("Raw Energizium Ore", 10, [PowerUpItemAction(10)], fg=[255, 0, 255], character='&')