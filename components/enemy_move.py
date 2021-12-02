from components.position import Position
from util.pathfinding import Pathfinding
from .component import Component
from .renderer import Renderer
from entities.entity import Entity
from engine.gamestate import GameState

class EnemyMove (Component):
    def __init__ (self, position : Position, renderer : Renderer, closeness: int, parent : Entity or None = None):
        super().__init__(parent, GameState.ENEMYTURN)
        self.position = position
        self.renderer = renderer
        self.path = None
        self.closeness = closeness
        self.last_seen_player = None
        
    def move (self, game):
        playerpos = game.player.get_component(Position)
        
        if self.renderer.visible:
            self.path = Pathfinding.get_path(self.position.x, self.position.y, playerpos.x, playerpos.y)
        elif self.last_seen_player != None:
            self.path = Pathfinding.get_path(self.position.x, self.position.y, self.last_seen_player[0], self.last_seen_player[1])
        
        if self.path != None and ((len(self.path) > self.closeness) if self.renderer.visible != None else (True)) and not (self.path[0][0] == playerpos.x and self.path[0][1] == playerpos.y):
            self.position.set(self.path[0][0], self.path[0][1])
    
    def update(self, game):
        super().update(game)
        if self.renderer.visible:
            player_pos = game.player.get_component(Position)
            self.last_seen_player = (player_pos.x, player_pos.y)
    
