from entities.entity import Entity
from .component import Component
from .position import Position
from engine.gamestate import GameState

class Renderer (Component):
    def __init__ (self, position : Position, character : str or None = "$", fg : list or None = [255, 0, 255], bg : list or None = [0, 0, 0], non_visible_fg : list or None = [25, 25, 25], non_visible_bg : list or None = [0, 0, 0], always_visible : bool or None = False, render_on_late_update : bool or None = False, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.always_visible = always_visible
        if self.always_visible:
            self.seen = True
            self.visible = True
        else:
            self.seen = False
            self.visible = False        
        self.character = character
        self.fg = fg
        self.bg = bg
        self.position = position
        self.non_visible_fg = non_visible_fg
        self.non_visible_bg = non_visible_bg
        self.render_on_late_update = render_on_late_update
        
    def print_renderer_to_console (self, game):
        if self.seen == False:
            game.root_console.print(x=self.position.x, y=self.position.y, string=" ", fg=[0, 0, 0], bg=[0, 0, 0])
        elif not self.visible:
            game.root_console.print(x=self.position.x, y=self.position.y, string=self.character, fg=self.non_visible_fg, bg=self.non_visible_bg)
        else:
            game.root_console.print(x=self.position.x, y=self.position.y, string=self.character, fg=self.fg, bg=self.bg)
    
    def update (self, game) :
        super().update(game)
        if not self.render_on_late_update:
            self.print_renderer_to_console(game)
    
    def late_update (self, game) :
        super().late_update(game)
        if self.render_on_late_update:
            self.print_renderer_to_console(game)