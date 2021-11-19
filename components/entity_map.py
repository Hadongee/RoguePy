import random

from engine.gamestate import GameState
from .entity_group import EntityGroup
from entities.entity import Entity
from .position import Position
from math import floor

# Component to create a collection of entities with given positions
class EntityMap (EntityGroup):
    # entity_spawn_method should be a method in the form (x  int, y : int, width: int, height : int) -> Entity
    # All entities returned with entity_spawn_method must have a Position component
    def __init__ (self, game, position : Position, width : int, height : int, entity_spawn_method, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(game, parent=parent, update_on_gamestate=update_on_gamestate)
        self.width = width
        self.height = height
        self.position = position

        for y in range(0, width):
            for x in range(0, height):
                self.add_entity(game, entity_spawn_method(x, y, width, height))
                if self.children[x + y * width - 1].get_component(Position) == None:
                    print("Error: Trying to create EntityMapGrid of entity without Position component")
                    raise
                child_position = self.children[x + y * width].get_component(Position)
                child_position.set(self.position.x + x - floor(width/2), self.position.y + y - floor(height/2))      
                self.position.add_child(child_position)

    def get_entity (self, x : int, y : int):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            print("Error: Trying to access entity of EntityMapGrid out of range")
            raise
        return self.children[y * self.width + x]
    
    @staticmethod
    def MAPTYPE_SIMPLE (entity : Entity):
        def grid_method (x : int, y : int, width: int, height : int) -> Entity:
            return entity
        return grid_method

    @staticmethod
    def MAPTYPE_BOX (inner_entity : Entity, outer_entity : Entity):
        def grid_method (x : int, y : int, width: int, height : int) -> Entity:
            if x == 0 or y == 0 or x == width-1 or y == height-1:
                return outer_entity
            else:
                return inner_entity
        return grid_method
    
    @staticmethod
    def MAPTYPE_RANDOM (entity1 : Entity, entity2 : Entity, random_chance : float):
        def grid_method (x : int, y : int, width: int, height : int) -> Entity:
            if random.random() <= random_chance:
                return entity1
            else:
                return entity2
        return grid_method
    
    @staticmethod
    def MAPTYPE_MULTIMAP (entities : list, entity_map : list):
        def grid_method (x : int, y : int, width: int, height : int) -> Entity:
            return entities[entity_map[x + y * width]]
        return grid_method