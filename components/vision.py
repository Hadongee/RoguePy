from components.renderer import Renderer
from .component import Component
from .position import Position
from .solid import Solid
from entities.entity import Entity
from entities.tile_bedrock import BedrockTile
import math

class Vision (Component):
    
    def __init__ (self, parent : Entity, position : Position):
        super().__init__(parent)
        self.position = position
    
    def early_update (self, game):
        rendered_entities = game.get_entities_with_component(Renderer)
        for rendered_entity in rendered_entities:
            renderer = rendered_entity.get_component(Renderer)
            if not renderer.always_visible:
                renderer.visible = False
        
        #self.raycast(game, 0, self.position.y - 1)
        #self.raycast(game, 0, self.position.y + 1)
        #self.raycast(game, game.screen_width-1, self.position.y - 1)
        #self.raycast(game, game.screen_width-1, self.position.y + 1)
        #self.raycast(game, self.position.y - 1, 0)
        #self.raycast(game, self.position.x + 1, 0)
        #self.raycast(game, self.position.y - 1, game.screen_height-1)
        #self.raycast(game, self.position.x + 1, game.screen_height-1)
                
        for x in range(game.screen_width):
            self.raycast(game, x, 0)
            self.raycast(game, x, game.screen_height-1)

        for y in range(game.screen_height):
            self.raycast(game, 0, y)
            self.raycast(game, game.screen_width-1, y)
            
    def raycast (self, game, other_x : float, other_y : float):
        current_x = self.position.x
        current_y = self.position.y
        
        my_pos_x = (float)(self.position.x) + 0.5
        my_pos_y = (float)(self.position.y) + 0.5
        
        other_pos_x = (float)(other_x) + 0.5
        other_pos_y = (float)(other_y) + 0.5
        
        difference_pos_x = other_pos_x - my_pos_x
        difference_pos_y = other_pos_y - my_pos_y
        
        angle = math.atan2(difference_pos_y, difference_pos_x)
        
        #print(f'angle: {angle}')
        
        hit_solid = 0

        while hit_solid <= 0:
            next_x = (int)(current_x + (difference_pos_x / abs(difference_pos_x)) if difference_pos_x != 0 else 0)
            next_y = (int)(current_y + (difference_pos_y / abs(difference_pos_y)) if difference_pos_y != 0 else 0)
            
            next_next_x = (int)(next_x + (difference_pos_x / abs(difference_pos_x)) if difference_pos_x != 0 else 0)
            next_next_y = (int)(next_y + (difference_pos_y / abs(difference_pos_y)) if difference_pos_y != 0 else 0)
            
            next_x_y = my_pos_y + math.tan(angle)*(next_x-my_pos_x)
            next_y_x = my_pos_x + ((next_y-my_pos_y)/math.tan(angle)) if math.tan(angle) != 0 else (float)(1000)
            
            dist_next_x = math.sqrt((next_x-my_pos_x)**2 + (next_x_y-my_pos_y)**2)
            dist_next_y = math.sqrt((next_y_x-my_pos_x)**2 + (next_y-my_pos_y)**2)
            
            #print(f'next_x: {next_x}, next_y: {next_y}, next_x_y: {next_x_y}, next_y_x: {next_y_x}, my_pos_x: {my_pos_x}, my_pos_y: {my_pos_y}')
            
            if abs(dist_next_x - dist_next_y) < 0.01:
                for entity in Position.entities_at_position[(next_x, next_y)]:
                    entity_renderer = entity.get_component(Renderer)
                    if entity_renderer != None:
                        entity_renderer.seen = True
                        entity_renderer.visible = True
                    if isinstance(entity, BedrockTile):
                        hit_solid += 1000
                    if entity.get_component(Solid) != None:
                        hit_solid += 1
                current_x = next_x
                my_pos_y = next_x_y
                current_y = next_y
                my_pos_x = next_y_x
            elif dist_next_x < dist_next_y:
                for entity in Position.entities_at_position[(next_x, current_y)]:
                    entity_renderer = entity.get_component(Renderer)
                    if entity_renderer != None:
                        entity_renderer.seen = True
                        entity_renderer.visible = True
                    if isinstance(entity, BedrockTile):
                        hit_solid += 1000
                    if entity.get_component(Solid) != None:
                        hit_solid += 1
                    else:
                        for entity in Position.entities_at_position[(next_x, next_y)]:
                            entity_renderer = entity.get_component(Renderer)
                            if entity_renderer != None and entity.get_component(Solid) != None:
                                entity_renderer.seen = True
                                entity_renderer.visible = True
                        for entity in Position.entities_at_position[(next_next_x, current_y)]:
                            entity_renderer = entity.get_component(Renderer)
                            if entity_renderer != None and entity.get_component(Solid) != None:
                                entity_renderer.seen = True
                                entity_renderer.visible = True
                        for entity in Position.entities_at_position[(next_next_x, next_y)]:
                            entity_renderer = entity.get_component(Renderer)
                            if entity_renderer != None and entity.get_component(Solid) != None:
                                entity_renderer.seen = True
                                entity_renderer.visible = True
                current_x = next_x
                my_pos_y = next_x_y
                my_pos_x = next_x
            elif dist_next_y < dist_next_x:
                for entity in Position.entities_at_position[(current_x, next_y)]:
                    entity_renderer = entity.get_component(Renderer)
                    if entity_renderer != None:
                        entity_renderer.seen = True
                        entity_renderer.visible = True
                    if isinstance(entity, BedrockTile):
                        hit_solid += 1000
                    if entity.get_component(Solid) != None:
                        hit_solid += 1
                    else:
                        for entity in Position.entities_at_position[(next_x, next_y)]:
                            entity_renderer = entity.get_component(Renderer)
                            if entity_renderer != None and entity.get_component(Solid) != None:
                                entity_renderer.seen = True
                                entity_renderer.visible = True
                        for entity in Position.entities_at_position[(current_x, next_next_y)]:
                            entity_renderer = entity.get_component(Renderer)
                            if entity_renderer != None and entity.get_component(Solid) != None:
                                entity_renderer.seen = True
                                entity_renderer.visible = True
                        for entity in Position.entities_at_position[(next_x, next_next_y)]:
                            entity_renderer = entity.get_component(Renderer)
                            if entity_renderer != None and entity.get_component(Solid) != None:
                                entity_renderer.seen = True
                                entity_renderer.visible = True
                current_y = next_y
                my_pos_x = next_y_x
                my_pos_y = next_y