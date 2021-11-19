from components.component import Component
from engine.actions import Action, LookAction
from entities.entity import Entity
from engine.gamestate import GameState

class ActionComponentEnabler (Component):
    def __init__ (self, components: list, action : type, parent : Entity or None = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        super().__init__(parent, update_on_gamestate)
        self.components = components
        self.action = action

    def handler_action (self, action):
        for component in self.components:
            component_on_entity = self.entity.get_component(component)
            if component_on_entity:
                if component_on_entity.enabled:
                    component_on_entity.enabled = False
                else:
                    component_on_entity.enabled = True

    def bind (self):
        Action.add_action(self.action, self.handler_action)