from .item import Item
from .item_actions import DropItemAction

class RawStoneItem (Item):
    def __init__ (self):
        super().__init__("Raw Stone Boulder", 1, [], fg=[100, 100, 100], character='o')