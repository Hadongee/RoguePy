from components.enemy_controller import EnemyController
from components.enemy_move import EnemyMove
from components.enemy_renderer import EnemyRenderer
from components.health import Health
from components.melee_attack import MeleeAttack
from components.unmovable import Unmovable
from engine.gamestate import GameState
from .entity import Entity
from components.position import Position
from components.renderer import Renderer
from util.damage import Damage

class Slasher (Entity):
    def __init__ (self, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__(description="Slasher")
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(EnemyRenderer(self.get_component(Position), character="s", fg=[255, 0, 0], non_visible_fg=[50, 0, 0]))
        self.add_component(EnemyMove(self.get_component(Position), self.get_component(Renderer), 0))
        self.add_component(MeleeAttack(self.get_component(Position), Damage(8, 15), 1.9))
        self.add_component(EnemyController(self.get_component(EnemyMove), self.get_component(MeleeAttack), update_on_gamestate=GameState.ENEMYTURN))
        self.add_component(Health(20))
        self.add_component(Unmovable())