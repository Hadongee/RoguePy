from enum import Enum

class GameState (Enum):
    EVERYTHINGTURN = 0
    PLAYERTURN = 1
    ENEMYTURN = 2
    INVENTORY = 3