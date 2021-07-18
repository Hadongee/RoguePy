class Action:
    actions = dict()

    @classmethod
    def add_action (cls, action:type, function):
        if action not in Action.actions:
            cls.actions[action] = list()
        cls.actions[action].append(function)
        print("Added new action: " + str(action) + ", total of this action=" + str(len(cls.actions[action])) + ", total actions=" + str(len(cls.actions)))

class EscapeAction:
    pass

class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy