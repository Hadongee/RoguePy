from components.enemy_move import EnemyMove
from components.health import Health
from components.position import Position
from .melee_attack import MeleeAttack
from .component import Component
from entities.entity import Entity
from engine.gamestate import GameState

class EnemyController (Component):
    def __init__ (self, enemy_move : EnemyMove, melee_attack : MeleeAttack, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.enemy_move = enemy_move
        self.melee_attack = melee_attack
        self.seen = False
        
    def early_update(self, game):
        super().early_update(game)
        if self.seen:
            player_pos = game.player.get_component(Position)
            if self.melee_attack.can_attack(player_pos.x, player_pos.y):
                self.melee_attack.attack(game, player_pos.x, player_pos.y, game.player.get_component(Health))
            else:
                self.enemy_move.move(game)