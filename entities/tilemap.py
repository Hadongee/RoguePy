from entities.tile_grass import GrassTile
from entities.entity import Entity
from components.entity_map import EntityMap
from components.position import Position
from .tile import Tile
from .tile_solid import SolidTile

import random

class Tilemap (Entity):
    def __init__ (self, game, center_x : int, center_y : int, width : int, height : int):
        super().__init__()
        self.add_component(Position(center_x, center_y))
        self.add_component(EntityMap(game, self.get_component(Position), width, height, EntityMap.MAPTYPE_MULTIMAP([SolidTile(), GrassTile()], Tilemap.generate_tilemap(width, height, 0.55, 8, 4, 5))))
    
    @staticmethod
    def generate_tilemap (width : int, height : int, initial_alive_chance : float, step_count: int, starvation_count : int, birth_count : int, seed: int or None = random.randint(-100000, 100000)):
        tilemap = list()
        random.seed = seed;

        def alive_neighbours (x : int, y : int) -> int:
            total = 0

            for _x in range(-1, 2):
                for _y in range(-1, 2):
                    lookX = x + _x
                    lookY = y + _y
                    if _x == 0 and _y == 0:
                        continue
                    elif lookX < 0 or lookX >= width or lookY < 0 or lookY >= height:
                        return 8
                    elif tilemap[lookX + lookY * width] == 0:
                        total+=1
            
            return total

        # Initialize tilemap with random chance to be alive 
        for y in range(height):
            for x in range(width):
                if random.random() <= initial_alive_chance:
                    tilemap.append(0)
                else:
                    tilemap.append(1)

        for _ in range(step_count):
            new_tilemap = list()

            for y in range(height):
                for x in range(width):
                    neighbours = alive_neighbours(x, y)
                    
                    if tilemap[x + y * width] == 0:
                        if neighbours < starvation_count:
                            new_tilemap.append(1)
                        else:
                            new_tilemap.append(0)
                    else:
                        if neighbours > birth_count:
                            new_tilemap.append(0)
                        else:
                            new_tilemap.append(1)
            tilemap = new_tilemap

        # Run Simulation Steps
        # Find the Caves
        # Filter caves based on size
        # Return tilemap
        return tilemap        
