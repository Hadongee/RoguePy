# Base Component class for the ECS
from engine.gamestate import GameState

class Component:
    def __init__ (self, parent = None, update_on_gamestate : GameState or None = GameState.EVERYTHINGTURN):
        # enabled property, can be used later to turn off components without deleting them
        # NOT USED CURRENTLY!
        self.enabled = True
        self.entity = parent
        self.update_on_gamestate = update_on_gamestate

    # Called before each action, once per game loop
    def update (self, game):
        pass
    
    # Called before each action and update, once per game loop
    def early_update (self, game):
        pass
    
    # Called before each action and after update, once per game loop
    def late_update (self, game):
        pass

    # If listening for an action, add a 'bind' method that adds the action method
    # using Action.add_action(<action type>, <method>)
    # for clarity use format 'handler_<action type>' for the action method
    # Example can be seen in player_move.py