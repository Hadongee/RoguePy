from components.position import Position
from engine.animation import Animation, SingleAnimation
from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState

class Health (Component):
    def __init__ (self, max_health : int, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.max_health = max_health
        self.health = max_health
        
    def deal_damage(self, damage : int):
        from engine.game import Game
        self.health -= damage
        Animation.add_animation(SingleAnimation((self.entity.get_component(Position).x, self.entity.get_component(Position).y), '/', [255, 0, 0]))
        if self.health <= 0:
            Game.instance.del_entity(self.entity)
            from entities.player import Player
            if isinstance(self.entity, Player):
                exit(0)