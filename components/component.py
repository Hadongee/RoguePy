# Base Component class for the ECS
class Component:
    def __init__ (self):
        # enabled property, can be used later to turn off components without deleting them
        # NOT USED CURRENTLY!
        self.enabled = True

    # Called before each action, once per game loop
    def update (self, game):
        pass

    # If listening for an action, add a 'bind' method that adds the action method
    # using Action.add_action(<action type>, <method>)
    # for clarity use format 'handler_<action type>' for the action method
    # Example can be seen in player_move.py