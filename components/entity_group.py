from .component import Component
from entities.entity import Entity
from .position import Position
from engine.gamestate import GameState

import copy

# Component for creating a collection of the same entity
class EntityGroup (Component):
    def __init__ (self, game, count : int or None = 0, entity : Entity or None = None, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        # List of child entities
        self.children= list()

        for _ in range(count):
            # Initialize children as "None" objects
            if entity == None:
                self.children.append(None)
            # If an entity is given, deep copy it
            else:
                new_entity = copy.deepcopy(entity)
                self.add_entity(game, new_entity)
                
    # Add entity to children, use this instead of directly manipulating 'children'     
    def add_entity (self, game, entity : Entity):
        new_entity = copy.deepcopy(entity)
        new_entity.get_component(Position).__init__(0, 0, parent=new_entity)
        new_entity.get_component(Position).on_add_component()
        # Add to game entity list to trigger initialization methods
        game.add_entity(new_entity)
        self.children.append(new_entity)

    # TODO: Method to destroy child
    # Needs to delete from game as well