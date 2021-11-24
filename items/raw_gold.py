from .item import Item
from .item_actions import DropItemAction

class RawGoldItem (Item):
    def __init__ (self):
        super().__init__("Raw Gold Ore", 24, [], fg=[255, 255, 0], character='*')