class Item () :
    def __init__ (self, name : str, maximum_stack : int, item_actions: list, fg : list or None = [255, 255, 255], bg : list or None = [0, 0, 0], character : str or None = "o"):
        self.name = name
        self.maximum_stack = maximum_stack
        self.item_actions = item_actions
        self.fg = fg
        self.bg = bg
        self.character = character