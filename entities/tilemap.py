from entities.tile_energizium import EnergiziumTile
from entities.tile_grass import GrassTile
from entities.entity import Entity
from components.entity_map import EntityMap
from components.position import Position
from .tile_stone import StoneTile
from .tile_bedrock import BedrockTile

import random

class Tilemap (Entity):
    def __init__ (self, game, center_x : int, center_y : int, width : int, height : int):
        super().__init__()
        self.tilemap = Tilemap.generate_tilemap(width, height, 0.575, 8, 4, 5, 0.015)
        self.add_component(Position(center_x, center_y))
        self.add_component(EntityMap(game, self.get_component(Position), width, height, EntityMap.MAPTYPE_MULTIMAP([StoneTile(), GrassTile(), BedrockTile(), EnergiziumTile()], self.tilemap)))
    
    @staticmethod
    def generate_tilemap (width : int, height : int, initial_alive_chance : float, step_count: int, starvation_count : int, birth_count : int, gold_chance : float, seed: int or None = random.randint(-100000, 100000)):
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
                    elif lookX <= 0 or lookX >= width-1 or lookY <= 0 or lookY >= height-1:
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

        # Run Simulation Steps
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

        found_caves = Tilemap.get_areas_from_tilemap(tilemap, width, height)

        # Filter caves based on size
        # Too small and they are deleted
        for cave in found_caves:
            if len(cave) < 32:
                for tile in cave:
                    tilemap[tile[0] + tile[1] * width] = 0

        # Set border to bedrock
        for y in range(height):
            for x in range(width):
                if y == 0 or y == height-1 or x == 0 or x == width-1:
                    tilemap[x + y * width] = 2

        # Place Gold :)
        for y in range(1, height-1):
            for x in range(1, width-1):
                if tilemap[x + y * width] == 0 and random.random() <= gold_chance:
                    tilemap[x + y * width] = 3

        # Return tilemap
        return tilemap

    @staticmethod
    def get_areas_from_tilemap (tilemap, width : int, height : int):
        # Find the Caves
        found_caves = list()
        found_cave_tiles = list()
        for y in range(height):
            for x in range(width):
                if tilemap[x + y * width] == 1:
                    if (x, y) not in found_cave_tiles:
                        found = list()
                        searching = list()
                        searching.append((x, y))
                        while len(searching) > 0:
                            current = searching.pop(0)
                            found.append(current)
                            for _x in range(-1, 2):
                                if _x == 0:
                                    continue
                                check = (current[0] + _x, current[1])
                                if tilemap[check[0] + check[1] * width] == 1 and not (check in searching or check in found):
                                    searching.append(check)
                            for _y in range(-1, 2):
                                if _y == 0:
                                    continue
                                check = (current[0], current[1] + _y)
                                if tilemap[check[0] + check[1] * width] == 1 and not (check in searching or check in found):
                                    searching.append(check)
                        
                        found_caves.append(found)

                        for found_tile in found:
                            found_cave_tiles.append(found_tile)
        
        return found_caves

        

                
