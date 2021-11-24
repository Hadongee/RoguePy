from components.inventory import Inventory
from engine.actions import Action, InventoryOpenAction, InventoryCloseAction, InventoryMoveAction, InventorySelectAction, InventoryTabAction
from engine.gamestate import GameState
from engine.input_handlers import EventHandlerState
from items.equipment_item import EquipmentItem

class InventoryRenderer ():
    def __init__ (self, inventory : Inventory, game):
        self.inventory = inventory
        self.game = game
        self.item_selected = 0
        self.item_action_selected = 0
        self.left_percentage = 0.7
        self.center_line_pos = (int)(self.game.game_width * self.left_percentage)
        self.right_start = self.center_line_pos + 1
        self.selecting_items = True
        
    def display_inventory (self):
        self.game.root_console.print(x=1, y=1, string=f"Inventory", fg=[255, 255, 255], bg=[0, 0, 0])
        self.game.root_console.print(x=self.center_line_pos+1, y=1, string=f"Item Actions", fg=[255, 255, 255], bg=[0, 0, 0])
        
        for item_index in range(len(self.inventory.items)):
            self.game.root_console.print(x=1, y=3 + item_index, string=f"    {self.inventory.items[item_index]['item'].name} " + (f"({self.inventory.items[item_index]['stack_size']})" if self.inventory.items[item_index]['stack_size'] > 1 else f"") + (f"E({self.inventory.items[item_index]['item'].equipped.name[0]})" if isinstance(self.inventory.items[item_index]['item'], EquipmentItem) and self.inventory.items[item_index]['item'].equipped != None else ""), fg=[255, 255, 255], bg=[0, 0, 0])
            self.game.root_console.print(x=3, y=3 + item_index, string=f"{self.inventory.items[item_index]['item'].character}", fg=self.inventory.items[item_index]['item'].fg, bg=self.inventory.items[item_index]['item'].bg)
        if len(self.inventory.items) > 0 and self.selecting_items:
            self.game.root_console.print(x=1, y=3 + self.item_selected, string=f">", fg=[255, 255, 255], bg=[0, 0, 0])
        
        if self.item_selected >= 0 and self.item_selected < len(self.inventory.items):
            for i in range(len(self.inventory.items[self.item_selected]["item"].item_actions)):
                self.game.root_console.print(x=self.center_line_pos+1, y=3 + i, string=f"  {self.inventory.items[self.item_selected]['item'].item_actions[i].name}", fg=[255, 255, 255], bg=[0, 0, 0])
            if len(self.inventory.items[self.item_selected]["item"].item_actions) > 0 and not self.selecting_items:
                self.game.root_console.print(x=self.right_start, y=3 + self.item_action_selected, string=f">", fg=[255, 255, 255], bg=[0, 0, 0])
        
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
        self.selecting_items = True

    def handler_InventoryCloseAction (self, action : InventoryCloseAction):
        self.game.gamestate = GameState.PLAYERTURN
        
    def handler_InventoryMoveAction (self, action : InventoryMoveAction):
        if self.selecting_items:
            self.item_selected += action.change
            if self.item_selected < 0:
                self.item_selected = 0
            if self.item_selected > len(self.inventory.items)-1:
                self.item_selected = len(self.inventory.items)-1
        elif (len(self.inventory.items) > 0):
            self.item_action_selected += action.change
            if self.item_action_selected < 0:
                self.item_action_selected = 0
            if self.item_action_selected > len(self.inventory.items[self.item_selected]["item"].item_actions)-1:
                self.item_action_selected = len(self.inventory.items[self.item_selected]["item"].item_actions)-1
    
    def handler_InventoryTabAction (self, action : InventoryTabAction):
        self.selecting_items = not self.selecting_items
        self.item_action_selected = 0
        
    def handler_InventorySelectAction (self, action : InventorySelectAction):
        if not self.selecting_items:
            if len(self.inventory.items) > 0:
                if len(self.inventory.items[self.item_selected]["item"].item_actions) > 0:
                    self.inventory.items[self.item_selected]["item"].item_actions[self.item_action_selected].on_use(self.inventory.items[self.item_selected], self.game)
                    self.game.event_handler.state = EventHandlerState.MAIN
                    self.game.gamestate = GameState.PLAYERTURN
                    self.game.event_handler.update_game_entities = True
    
    def bind (self) :
        Action.add_action(InventoryOpenAction, self.handler_InventoryOpenAction)
        Action.add_action(InventoryCloseAction, self.handler_InventoryCloseAction)
        Action.add_action(InventoryMoveAction, self.handler_InventoryMoveAction)
        Action.add_action(InventoryTabAction, self.handler_InventoryTabAction)
        Action.add_action(InventorySelectAction, self.handler_InventorySelectAction)