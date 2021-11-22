class Action:
    actions = dict()

    def __init__ (self, update_game_entities : bool or None = True):
        self.update_game_entities = update_game_entities
    
    @classmethod
    def add_action (cls, action:type, function):
        if action not in Action.actions:
            cls.actions[action] = list()
        cls.actions[action].append(function)
        print("Added new action: " + str(action) + ", total of this action=" + str(len(cls.actions[action])) + ", total actions=" + str(len(cls.actions)))

class EscapeAction (Action):
    def __init__ (self):
        super().__init__(False)

class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
        
class CursorMovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

class WaitAction(Action):
    def __init__(self):
        super().__init__()
        
class DigToggleAction(Action):
    def __init__(self):
        super().__init__()
        
class LookToggleAction(Action):
    def __init__(self):
        super().__init__()

class PickupToggleAction(Action):
    def __init__(self):
        super().__init__()
        
class DigAction (Action):
    def __init__(self):
        super().__init__()
        
class PickupAction (Action):
    def __init__(self):
        super().__init__()

class InventoryOpenAction (Action):
    def __init__(self):
        super().__init__(False)
        
class InventoryCloseAction (Action):
    def __init__(self):
        super().__init__(True)
        
class InventoryMoveAction (Action):
    def __init__(self, change : int):
        super().__init__(False)
        
        self.change = change

class DigMovementAction (Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy
        
class PickupMovementAction (Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy