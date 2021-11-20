from components.component import Component
from engine.gamestate import GameState

class Entity :
    def __init__ (self, description : str or None = "An entity", *components : Component):
        self.description = description
        self.components = list()
        for component in components:
            self.add_component(component)

    def update (self, game):
        for component in self.components:
            if component.enabled and (component.update_on_gamestate == GameState.EVERYTHINGTURN or component.update_on_gamestate == game.gamestate):
                component.update(game)
            
    def early_update (self, game):
        for component in self.components:
            if component.enabled and (component.update_on_gamestate == GameState.EVERYTHINGTURN or component.update_on_gamestate == game.gamestate):
                component.early_update(game)
    
    def late_update (self, game):
        for component in self.components:
            if component.enabled and (component.update_on_gamestate == GameState.EVERYTHINGTURN or component.update_on_gamestate == game.gamestate):
                component.late_update(game)

    def add_component (self, component: Component):
        self.components.append(component)
        self.components[len(self.components)-1].entity = self
        if hasattr(self.components[len(self.components)-1], "on_add_component") == True:
            self.components[len(self.components)-1].on_add_component()

    def del_component (self, component: Component):
        self.components.remove(component)
    
    def get_component (self, component_type : type):
        for component in self.components:
            if type(component) == component_type:
                return component
        return None

