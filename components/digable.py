from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState
from .position import Position
import copy

class Digable (Component) :
    def __init__ (self, position : Position, entities_dropped : list or None = None, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.entities_dropped = entities_dropped
        self.position = position
        
    def on_dig (self, game):
        game.del_entity(self.entity)
        for entity in self.entities_dropped:
            if isinstance(entity, Entity):
                new_entity = copy.deepcopy(entity)
                new_entity.get_component(Position).__init__(self.position.x, self.position.y, parent=new_entity)
                new_entity.get_component(Position).on_add_component()
                
                game.add_entity(new_entity)
        
        