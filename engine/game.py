from components.health import Health
from components.inventory import Inventory
from entities.drop_pod import DropPod
from entities.slasher import Slasher
import tcod
import random
import copy

from util.pathfinding import Pathfinding

from .actions import Action, EscapeAction, MovementAction
from .input_handlers import EventHandler
from .settings_handler import Settings, SettingsHandler
from .gamestate import GameState
from .inventory_renderer import InventoryRenderer
from entities.entity import Entity
from entities.player import Player
from entities.entity import Entity
from entities.tilemap import Tilemap
from entities.cursor import Cursor
from components.player_stats import PlayerStats
from components.position import Position
from engine.gamestate import GameState

class Game :
    instance = None
    def __init__ (self):
        if Game.instance != None:
            print("ERROR: Creating more than one instance of Game class")
        else: 
            Game.instance = self
        self.settings = SettingsHandler().settings
        self.pathfinding = Pathfinding(self)

        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height
        
        self.game_width = self.screen_width
        self.game_height = self.screen_height - 5

        self.tileset = tcod.tileset.load_tilesheet(self.settings.tilesheet, self.settings.tilesheet_width, self.settings.tilesheet_height, tcod.tileset.CHARMAP_CP437)

        self.event_handler = EventHandler(self)
        self.gamestate = GameState.PLAYERTURN
        self.update_enemies = True

        self.entities = list()

        tilemap = Tilemap(self, int(self.game_width/2), int(self.game_height/2), self.game_width, self.game_height)
        self.add_entity(tilemap)
        
        caves = Tilemap.get_areas_from_tilemap(tilemap.tilemap, self.game_width, self.game_height)
        biggest_cave = caves[0]
        for cave in caves:
            if len(cave) > len(biggest_cave):
                biggest_cave = cave
        spawnpoint = random.choice(biggest_cave)

        self.add_entity(Player(self, spawnpoint[0], spawnpoint[1]))
        self.player = self.entities[len(self.entities) - 1]
        
        self.inventory_renderer = InventoryRenderer(self.player.get_component(Inventory), self)
        self.inventory_renderer.bind()
        
        self.add_entity(Cursor(self, int(self.game_width/2), int(self.game_height/2)))
        
        for _ in range(1):
            drop_spawnpoint = random.choice(biggest_cave)
            while drop_spawnpoint == spawnpoint:
                drop_spawnpoint = random.choice(biggest_cave)
            self.add_entity(Slasher(drop_spawnpoint[0], drop_spawnpoint[1]))

    def add_entity (self, entity : Entity):
        self.entities.append(entity)
        if hasattr(entity, "on_created") == True:
            entity.on_created()
        for component in entity.components:
            if hasattr(component, "bind") == True:
                component.bind()
                
    def update_entities (self, context):
        if self.event_handler.update_game_entities:
            print("---------UPDATING ENTITIES---------")
            self.root_console.clear()
            for entity in self.entities:
                entity.early_update(self)
            for entity in self.entities:
                entity.update(self)
            for entity in self.entities:
                entity.late_update(self)
        
        self.root_console.print(x=0, y=self.screen_height-5, string=f"Health: ", fg=[255, 0, 0], bg=[0, 0, 0])
        self.root_console.print(x=8, y=self.screen_height-5, string=f"{self.player.get_component(Health).health}", fg=[255, 255, 255], bg=[0, 0, 0])
        self.root_console.print(x=14, y=self.screen_height-5, string=f"Energy: ", fg=[0, 255, 0], bg=[0, 0, 0])
        self.root_console.print(x=22, y=self.screen_height-5, string=f"{self.player.get_component(PlayerStats).energy}", fg=[255, 255, 255], bg=[0, 0, 0])
        
        context.present(self.root_console, keep_aspect=True)
    
    def del_entity (self, entity : Entity):
        if entity in self.entities:
            self.entities.remove(entity)
        position_of_entity = entity.get_component(Position)
        if position_of_entity != None:
            Position.entities_at_position[(position_of_entity.x, position_of_entity.y)].remove(entity)
    
    def get_entities_with_component (self, component_type : type):
        entities_with_component = list()
        for entity in Game.instance.entities:
            if entity.get_component(component_type) != None:
                entities_with_component.append(entity)
        return entities_with_component                

    def start_game_loop (self):
        with tcod.context.new_terminal(
            self.screen_width, self.screen_height, tileset=self.tileset, title=self.settings.title, vsync=self.settings.vsync, sdl_window_flags=tcod.context.SDL_WINDOW_MAXIMIZED
        ) as context:
            self.root_console = tcod.Console(self.screen_width, self.screen_height, order="F")
            while True:
                if self.gamestate != GameState.INVENTORY:
                    self.update_entities(context)
                    if self.update_enemies:
                        self.gamestate = GameState.ENEMYTURN
                        self.update_entities(context)
                        self.gamestate = GameState.PLAYERTURN
                else:
                    self.root_console.clear()
                    self.inventory_renderer.display_inventory()
                    context.present(self.root_console, keep_aspect=True)
                
                self.event_handler.update_game_entities = False

                for event in tcod.event.wait():
                    action = self.event_handler.dispatch(event)

                    if action is None:
                        continue
                    elif isinstance(action, EscapeAction):
                        raise SystemExit()
                        continue
                    for key, actions in Action.actions.items():
                        if type(action) == key:
                            for handler in actions:
                                handler(action)
                            break