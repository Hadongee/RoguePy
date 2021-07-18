from .component import Component


class Position (Component):
    def __init__ (self, x : int or None = 0, y : int or None = 0):
        super().__init__()
        self.x = x
        self.y = y
        self.children = list()

    def move (self, dx : int, dy : int):
        self.x += dx
        self.y += dy
        for child in self.children:
            child.move(dx, dy)
        #print("Moving: " + str(self) + " typeof " + str(type(self)) + " by " + Position(dx, dy).to_string() + " to " + self.to_string())
    
    def set (self, x : int, y : int):
        self.x = x
        self.y = y
        for child in self.children:
            child.set(x, y)

    def add_child(self, child : 'Position'):
        self.children.append(child)

    def to_string (self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
