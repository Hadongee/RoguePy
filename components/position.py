from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState

class Position (Component):
    entities_at_position = dict()
    
    def __init__ (self, x : int or None = 0, y : int or None = 0, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.x = x
        self.y = y
        self.children = list()
        
    def on_add_component (self):
        if (self.x, self.y) not in Position.entities_at_position:
            Position.entities_at_position[(self.x, self.y)] = list()
        Position.entities_at_position[(self.x, self.y)].append(self.entity)

    def move (self, dx : int, dy : int):
        Position.entities_at_position[(self.x, self.y)].remove(self.entity)
        self.x += dx
        self.y += dy
        if (self.x, self.y) not in Position.entities_at_position:
            Position.entities_at_position[(self.x, self.y)] = list()
        Position.entities_at_position[(self.x, self.y)].append(self.entity)
        for child in self.children:
            child.move(dx, dy)
        #print("Moving: " + str(self) + " typeof " + str(type(self)) + " by " + Position(dx, dy).to_string() + " to " + self.to_string())
    
    def set (self, x : int, y : int):
        
        Position.entities_at_position[(self.x, self.y)].remove(self.entity)
        self.x = x
        self.y = y
        if (self.x, self.y) not in Position.entities_at_position:
            Position.entities_at_position[(self.x, self.y)] = list()
        Position.entities_at_position[(self.x, self.y)].append(self.entity)
        for child in self.children:
            child.set(x, y)

    def add_child(self, child : 'Position'):
        self.children.append(child)

    def to_string (self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
