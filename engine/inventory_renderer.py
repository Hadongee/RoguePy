from components.inventory import Inventory
from engine.actions import Action, InventoryOpenAction, InventoryCloseAction, InventoryMoveAction
from engine.gamestate import GameState

class InventoryRenderer ():
    def __init__ (self, inventory : Inventory, game):
        self.inventory = inventory
        self.game = game
        self.item_selected = 0
        self.left_percentage = 0.6
        self.center_line_pos = (int)(self.game.game_width * self.left_percentage)
        self.right_start = self.center_line_pos + 1
        
    def display_inventory (self):
        self.game.root_console.print(x=1, y=1, string=f"Inventory", fg=[255, 255, 255], bg=[0, 0, 0])
        self.game.root_console.print(x=self.center_line_pos+1, y=1, string=f"Item Actions", fg=[255, 255, 255], bg=[0, 0, 0])
        for item_index in range(len(self.inventory.items)):
            self.game.root_console.print(x=1, y=3 + item_index, string=f"  {self.inventory.items[item_index].name}", fg=[255, 255, 255], bg=[0, 0, 0])
        self.game.root_console.print(x=1, y=3 + self.item_selected, string=f">", fg=[255, 255, 255], bg=[0, 0, 0])
        
        for i in range(self.game.game_height):
            self.game.root_console.print(x=self.center_line_pos, y=i, string="║", fg=[200, 200, 200], bg=[0, 0, 0])
            self.game.root_console.print(x=0, y=i, string="║", fg=[200, 200, 200], bg=[0, 0, 0])
            self.game.root_console.print(x=self.game.game_width-1, y=i, string="║", fg=[200, 200, 200], bg=[0, 0, 0])
        
        for i in range(self.game.game_width):
            self.game.root_console.print(x=i, y=0, string="═", fg=[200, 200, 200], bg=[0, 0, 0])
            self.game.root_console.print(x=i, y=2, string="═", fg=[200, 200, 200], bg=[0, 0, 0])
            self.game.root_console.print(x=i, y=self.game.game_height-1, string="═", fg=[200, 200, 200], bg=[0, 0, 0])
        
        self.game.root_console.print(x=0, y=self.game.game_height-1, string="╚", fg=[200, 200, 200], bg=[0, 0, 0])
        self.game.root_console.print(x=self.game.game_width-1, y=self.game.game_height-1, string="╝", fg=[200, 200, 200], bg=[0, 0, 0])
        self.game.root_console.print(x=0, y=0, string="╔", fg=[200, 200, 200], bg=[0, 0, 0])
        self.game.root_console.print(x=self.game.game_width-1, y=0, string="╗", fg=[200, 200, 200], bg=[0, 0, 0])
        self.game.root_console.print(x=self.center_line_pos, y=0, string="╦", fg=[200, 200, 200], bg=[0, 0, 0])
        self.game.root_console.print(x=self.center_line_pos, y=self.game.game_height-1, string="╩", fg=[200, 200, 200], bg=[0, 0, 0])
        self.game.root_console.print(x=self.center_line_pos, y=2, string="╬", fg=[200, 200, 200], bg=[0, 0, 0])
        self.game.root_console.print(x=0, y=2, string="╠", fg=[200, 200, 200], bg=[0, 0, 0])
        self.game.root_console.print(x=self.game.game_width-1, y=2, string="╣", fg=[200, 200, 200], bg=[0, 0, 0])
    
    def handler_InventoryOpenAction (self, action : InventoryOpenAction):
        self.game.gamestate = GameState.INVENTORY
        self.item_selected = 0

    def handler_InventoryCloseAction (self, action : InventoryCloseAction):
        self.game.gamestate = GameState.EVERYTHINGTURN
        
    def handler_InventoryMoveAction (self, action : InventoryMoveAction):
        self.item_selected += action.change
        if self.item_selected < 0:
            self.item_selected = 0
        if self.item_selected > len(self.inventory.items)-1:
            self.item_selected = len(self.inventory.items)-1
    
    def bind (self) :
        Action.add_action(InventoryOpenAction, self.handler_InventoryOpenAction)
        Action.add_action(InventoryCloseAction, self.handler_InventoryCloseAction)
        Action.add_action(InventoryMoveAction, self.handler_InventoryMoveAction)