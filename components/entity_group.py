from .component import Component
from entities.entity import Entity

import copy

class EntityGroup (Component):
    def __init__ (self, game, count : int or None = 0, entity : Entity or None = None):
        super().__init__()
        self.children= list()
        for _ in range(count):
            if entity == None:
                self.children.append(None)
            else:
                new_entity = copy.deepcopy(entity)
                self.add_entity(game, new_entity)
                
        
    def add_entity (self, game, entity : Entity):
        new_entity = copy.deepcopy(entity)
        game.add_entity(new_entity)
        self.children.append(new_entity)