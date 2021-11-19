from .component import Component
from .position import Position
from entities.entity import Entity
from engine.gamestate import GameState
from .renderer import Renderer

class CursorLook (Component):
    def __init__ (self, position : Position, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.position = position

    def late_update(self, game):
        super().late_update(game)
        
        if len(Position.entities_at_position[(self.position.x, self.position.y)]) > 1:
            entity_at_pos = Position.entities_at_position[(self.position.x, self.position.y)][len(Position.entities_at_position[(self.position.x, self.position.y)])-2]
            if entity_at_pos.get_component(Renderer) and entity_at_pos.get_component(Renderer).seen:
                description = entity_at_pos.description
            else:
                description = "???"
            print(f"lookin at {self.position.x}, {self.position.y}, entity={entity_at_pos}, description={description}")
            game.root_console.print(x=0, y=game.screen_height-4, string=f"{description}", fg=[255, 255, 255], bg=[0, 0, 0])
        else:
            game.root_console.print(x=0, y=game.screen_height-4, string=f"ERROR: NO ENTITY", fg=[255, 255, 255], bg=[0, 0, 0])