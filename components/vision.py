from components.renderer import Renderer
from .component import Component
from .position import Position
from .solid import Solid
from entities.entity import Entity
from entities.tile_bedrock import BedrockTile
from engine.gamestate import GameState
import math

class Vision (Component):
    
    def __init__ (self, position : Position, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
    
    def early_update (self, game):
        rendered_entities = game.get_entities_with_component(Renderer)
        for rendered_entity in rendered_entities:
            renderer = rendered_entity.get_component(Renderer)
            if not renderer.always_visible:
                renderer.visible = False
                
        for x in range(game.game_width):
            tiles_hit = self.raycast(x, 0, True)
            self.reveal_in_raycast(tiles_hit, self.sign(x-self.position.x), -1)
            
            tiles_hit = self.raycast(x, game.game_height-1, True)
            self.reveal_in_raycast(tiles_hit, self.sign(x-self.position.x), 1)

        for y in range(game.game_height):
            tiles_hit = self.raycast(0, y, True)
            self.reveal_in_raycast(tiles_hit, -1, self.sign(y-self.position.y))
            
            tiles_hit = self.raycast(game.game_width-1, y, True)
            self.reveal_in_raycast(tiles_hit, 1, self.sign(y-self.position.y))

    def sign (self, num: float):
        if num > 0:
            return 1
        elif num < 0:
            return -1
        else:
            return 0
    
    def reveal_in_raycast (self, cast : list, x_direction : int, y_direction : int):
        for tile in cast:
            for entity in Position.entities_at_position[tile]:
                self.reveal_entity(entity)
        if len(cast) > 1:
            wall_fix_tile_x = cast[-2][0] + x_direction
            wall_fix_tile_y = cast[-2][1] + y_direction
            for entity in Position.entities_at_position[(wall_fix_tile_x, wall_fix_tile_y)]:
                if entity.get_component(Solid) != None:
                    self.reveal_entity(entity)
            
    def reveal_entity (self, entity : Entity):
        from .enemy_controller import EnemyController
        entity_renderer = entity.get_component(Renderer)
        if entity_renderer != None:
            entity_renderer.seen = True
            entity_renderer.visible = True
        entity_enemy = entity.get_component(EnemyController)
        if entity_enemy != None:
            entity_enemy.seen = True
            
    def raycast (self, other_x : float, other_y : float, return_all : bool):
        current_x = self.position.x
        current_y = self.position.y
        
        my_pos_x = (float)(self.position.x) + 0.5
        my_pos_y = (float)(self.position.y) + 0.5
        
        other_pos_x = (float)(other_x) + 0.5
        other_pos_y = (float)(other_y) + 0.5
        
        difference_pos_x = other_pos_x - my_pos_x
        difference_pos_y = other_pos_y - my_pos_y
        
        angle = math.atan2(difference_pos_y, difference_pos_x)
        
        tile_passthrough = list()
        
        hit_solid = 0
        distance = 0

        while hit_solid <= 0 and not (current_x == other_x and current_y == other_y):
            next_x = (int)(current_x + (difference_pos_x / abs(difference_pos_x)) if difference_pos_x != 0 else 0)
            next_y = (int)(current_y + (difference_pos_y / abs(difference_pos_y)) if difference_pos_y != 0 else 0)
            
            next_x_y = my_pos_y + math.tan(angle)*(next_x-my_pos_x)
            next_y_x = my_pos_x + ((next_y-my_pos_y)/math.tan(angle)) if math.tan(angle) != 0 else (float)(1000)
            
            dist_next_x = math.sqrt((next_x-my_pos_x)**2 + (next_x_y-my_pos_y)**2)
            dist_next_y = math.sqrt((next_y_x-my_pos_x)**2 + (next_y-my_pos_y)**2)

            if abs(dist_next_x - dist_next_y) < 0.001:
                tile_passthrough.append((next_x, next_y))
                for entity in Position.entities_at_position[(next_x, next_y)]:
                    if isinstance(entity, BedrockTile):
                        hit_solid += 1000
                        break
                    if entity.get_component(Solid) != None:
                        hit_solid += 1
                        break
                current_x = next_x
                my_pos_y = next_x_y
                current_y = next_y
                my_pos_x = next_y_x
                distance += dist_next_x
            elif dist_next_x < dist_next_y:
                tile_passthrough.append((next_x, current_y))
                for entity in Position.entities_at_position[(next_x, current_y)]:
                    if isinstance(entity, BedrockTile):
                        hit_solid += 1000
                        break
                    if entity.get_component(Solid) != None:
                        hit_solid += 1
                        break
                current_x = next_x
                my_pos_y = next_x_y
                my_pos_x = next_x
                distance += dist_next_x
            elif dist_next_y < dist_next_x:
                tile_passthrough.append((current_x, next_y))
                for entity in Position.entities_at_position[(current_x, next_y)]:
                    if isinstance(entity, BedrockTile):
                        hit_solid += 1000
                        break
                    if entity.get_component(Solid) != None:
                        hit_solid += 1
                        break
                current_y = next_y
                my_pos_x = next_y_x
                my_pos_y = next_y
                distance += dist_next_y
        
        if return_all:
            return tile_passthrough
        else:
            return tile_passthrough[-1]