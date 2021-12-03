from components.health import Health
from components.position import Position
from engine.animation import Animation, SingleAnimation
from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState
from util.damage import Damage
import math

class MeleeAttack (Component):
    def __init__ (self, position : Position, damage : Damage, reach : float, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position
        self.reach = reach
        self.damage = damage
    
    def can_attack(self, x : int, y : int):
        if math.sqrt((x - self.position.x)**2 + (y - self.position.y)**2) < self.reach:
            return True
        else:
            return False
    
    def attack (self, game, x : int, y : int, health : Health):
        if self.can_attack(x, y):
            entities = Position.entities_at_position[(x, y)]
            for entity in entities:
                if entity.get_component(Health) != None:
                    damage = self.damage.get_random()
                    entity.get_component(Health).deal_damage(damage)
                    game.add_to_log(f"{self.entity.description} attacked you for {damage}")
                    #Animation.add_animation(SingleAnimation((x, y), '/', [255, 0, 0]))
                    break