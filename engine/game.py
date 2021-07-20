import tcod
import random

from .actions import Action, EscapeAction, MovementAction
from .input_handlers import EventHandler
from .settings_handler import Settings, SettingsHandler
from entities.player import Player
from components.position import Position
from components.entity_map import EntityMap
from entities.tile import Tile
from entities.tile_solid import SolidTile
from entities.entity import Entity
from entities.tilemap import Tilemap

class Game :
    def __init__ (self):
        self.settings = SettingsHandler().settings

        self.screen_width = self.settings.screen_width
        self.screen_height = self.settings.screen_height

        self.tileset = tcod.tileset.load_tilesheet(self.settings.tilesheet, self.settings.tilesheet_width, self.settings.tilesheet_height, tcod.tileset.CHARMAP_TCOD)

        self.event_handler = EventHandler()

        self.entities = list()

        tilemap = Tilemap(self, int(self.screen_width/2), int(self.screen_height/2), self.screen_width, self.screen_height)
        self.add_entity(tilemap)

        #entity_pos = Position(int(self.screen_width/2), int(self.screen_height/2))
        # self.add_entity(
        #     Entity(
        #         entity_pos,
        #         EntityMap(self, entity_pos, self.screen_width, self.screen_height, EntityMap.MAPTYPE_RANDOM(Tile(), SolidTile(), 0.7)),        
        #     )
        # )

        caves = Tilemap.get_areas_from_tilemap(tilemap.tilemap, self.screen_width, self.screen_height)
        biggest_cave = caves[0]
        for cave in caves:
            if len(cave) > len(biggest_cave):
                biggest_cave = cave
        spawnpoint = random.choice(biggest_cave)

        self.add_entity(Player(spawnpoint[0], spawnpoint[1]))

    def add_entity (self, entity : Entity):
        self.entities.append(entity)
        if hasattr(entity, "on_created") == True:
            entity.on_created()
        for component in entity.components:
            if hasattr(component, "bind") == True:
                component.bind()

    def start_game_loop (self):
        with tcod.context.new_terminal(
            self.screen_width, self.screen_height, tileset=self.tileset, title=self.settings.title, vsync=self.settings.vsync,
        ) as context:
            self.root_console = tcod.Console(self.screen_width, self.screen_height, order="F")
            while True:
                for entity in self.entities:
                    entity.update(self)

                context.present(self.root_console)

                self.root_console.clear()

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