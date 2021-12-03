from components.position import Position
from components.solid import Solid
import math
from components.unmovable import Unmovable

from entities.player import Player

class Pathfinding ():
    def __init__ (self, game):
        Pathfinding.game = game
        pass
    
    @classmethod
    def get_path (cls, start_x : int, start_y : int, end_x : int, end_y : int):
        
        def euclidean_dist (current_x : int, current_y : int):
            return math.sqrt((end_x - current_x)**2 + (end_y - current_y)**2)
        
        camefrom = list()
        
        width = cls.game.game_width
        height = cls.game.game_height
        
        def reconstruct ():
            path = list()
            look_node = (end_x, end_y)
            while camefrom[look_node[0] + look_node[1] * width] != None:
                path.append(look_node)
                look_node = camefrom[look_node[0] + look_node[1] * width]
            path.reverse()
            return path
        
        open_set = list()
        open_set.append((start_x, start_y))        
        
        gscore = list()
        fscore = list()
        for _ in range(height):
            for _ in range(width):
                camefrom.append(None)
                gscore.append(math.inf)
                fscore.append(math.inf)
                
        gscore[start_x + start_y * width] = 0
        fscore[start_x + start_y * width] = euclidean_dist(start_x, start_y)
    
        while len(open_set) > 0:
            current = None
            # Set current to the node in openset with the lowest fscore value
            lowest_value = math.inf
            for _node in open_set:
                if fscore[_node[0] + _node[1] * width] < lowest_value:
                    lowest_value = fscore[_node[0] + _node[1] * width]
                    current = _node
                    
            if current[0] == end_x and current[1] == end_y:
                return reconstruct()
            
            open_set.remove(current)
            
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if abs(dx) == abs(dy):
                        continue
                    distance = 1
                    for _entity in Position.entities_at_position[(current[0] + dx), (current[1] + dy)]:
                        if _entity.get_component(Solid) != None:
                            distance = math.inf
                            break
                        if _entity.get_component(Unmovable) != None:
                            distance = math.inf
                            break
                    tentative_gscore = gscore[current[0] + current[1] * width] + distance
                    neighbouring_index = (current[0] + dx) + (current[1] + dy) * width
                    if tentative_gscore < gscore[neighbouring_index]:
                        camefrom[neighbouring_index] = current
                        gscore[neighbouring_index] = tentative_gscore
                        fscore[neighbouring_index] = tentative_gscore + euclidean_dist(current[0] + dx, current[1] + dy)
                        for _node in open_set:
                            if _node[0] == current[0] + dx and _node[1] == current[1] + dy:
                                break
                        else:
                            open_set.append((current[0] + dx, current[1] + dy))
                                
        return None