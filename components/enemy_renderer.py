from components.renderer import Renderer
from entities.entity import Entity
from .component import Component
from .position import Position
from engine.gamestate import GameState

class EnemyRenderer (Renderer):
    def __init__ (self, position : Position, character : str or None = "$", fg : list or None = [255, 0, 255], bg : list or None = [0, 0, 0], non_visible_fg : list or None = [35, 35, 35], non_visible_bg : list or None = [0, 0, 0], always_visible : bool or None = False, render_on_late_update : bool or None = False, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(position, character, fg, bg, non_visible_fg, non_visible_bg, always_visible, render_on_late_update, parent, update_on_gamestate)
        self.last_seen = None
        
    def print_renderer_to_console (self, game):
        if self.seen == False:
            game.root_console.print(x=self.position.x, y=self.position.y, string=" ", fg=[0, 0, 0], bg=[0, 0, 0])
        elif not self.visible:
            game.root_console.print(x=self.last_seen[0], y=self.last_seen[1], string=self.character, fg=self.non_visible_fg, bg=self.non_visible_bg)
        else:
            self.last_seen = (self.position.x, self.position.y)
            game.root_console.print(x=self.position.x, y=self.position.y, string=self.character, fg=self.fg, bg=self.bg)
    
    def update (self, game) :
        super().update(game)
    
    def late_update (self, game) :
        super().late_update(game)