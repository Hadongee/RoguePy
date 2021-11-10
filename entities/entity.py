from components.component import Component

class Entity :
    def __init__ (self, *components : Component):
        self.components = list()
        for component in components:
            self.add_component(component)

    def update (self, game):
        for component in self.components:
            component.update(game)
            
    def early_update (self, game):
        for component in self.components:
            component.early_update(game)
    
    def late_update (self, game):
        for component in self.components:
            component.late_update(game)

    def add_component (self, component: Component):
        self.components.append(component)

    def del_component (self, component: Component):
        for _component in self.components:
            if type(_component) == type(component):
                self.components.remove(_component)
                return
    
    def get_component (self, component_type : type):
        for component in self.components:
            if type(component) == component_type:
                return component
        return None

