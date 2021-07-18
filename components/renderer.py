from .component import Component
from .position import Position

class Renderer (Component):
    def __init__ (self, character : str or None = "$", fg : list or None = [255, 0, 255], bg : list or None = [0, 0, 0], position : Position or None = Position()):
        super().__init__()
        self.character = character
        self.fg = fg
        self.bg = bg
        self.position = position
    
    def update (self, game) :
        super().update(game)
        game.root_console.print(x=self.position.x, y=self.position.y, string=self.character, fg=self.fg, bg=self.bg)