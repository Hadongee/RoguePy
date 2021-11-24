from components.equipment import Equipment
from components.inventory import Inventory
from components.player_stats import PlayerStats
from engine.gamestate import GameState
from items.basic_energy_pistol import BasicEnergyPistolItem
from items.basic_plasma_cutter import BasicPlasmaCutterItem
from items.basic_power_armour_body import BasicPowerArmourBodyItem
from items.basic_power_armour_feet import BasicPowerArmourFeetItem
from items.basic_power_armour_helmet import BasicPowerArmourHelmetItem
from items.basic_power_armour_legs import BasicPowerArmourLegsItem
from items.equipment_slot import EquipmentSlot
from .entity import Entity
from components.position import Position
from components.renderer import Renderer
from components.player_move import PlayerMove
from components.vision import Vision
from components.action_component_enabler import ActionComponentEnabler
from engine.actions import DigToggleAction, LookToggleAction, DigAction, PickupToggleAction, PickupAction
from engine.settings_handler import SettingsHandler

class Player (Entity):
    def __init__ (self, game, spawn_x : int or None = 0, spawn_y : int or None = 0):
        super().__init__()
        self.description = "Player"
        settings = SettingsHandler().settings
        self.add_component(Position(spawn_x, spawn_y))
        self.add_component(Renderer(self.get_component(Position), character="@", fg=[0, 255, 255], always_visible=True, render_on_late_update=True))
        self.add_component(PlayerMove(self.get_component(Position)))
        self.add_component(Vision(self.get_component(Position)))
        self.add_component(PlayerStats(settings.max_health, settings.max_energy))
        self.add_component(ActionComponentEnabler([Vision], LookToggleAction))
        self.add_component(ActionComponentEnabler([Vision], DigToggleAction))
        self.add_component(ActionComponentEnabler([Vision], DigAction))
        self.add_component(ActionComponentEnabler([Vision], PickupToggleAction))
        self.add_component(ActionComponentEnabler([Vision], PickupAction))
        self.add_component(Inventory(25))
        self.add_component(Equipment())
        
        inventory = self.get_component(Inventory)
        equipment = self.get_component(Equipment)
        inventory.add_item(BasicPowerArmourHelmetItem())
        equipment.equip_item(inventory.items[len(inventory.items)-1]['item'], EquipmentSlot.HEAD)
        inventory.add_item(BasicPowerArmourBodyItem())
        equipment.equip_item(inventory.items[len(inventory.items)-1]['item'], EquipmentSlot.TORSO)
        inventory.add_item(BasicPowerArmourLegsItem())
        equipment.equip_item(inventory.items[len(inventory.items)-1]['item'], EquipmentSlot.LEGS)
        inventory.add_item(BasicPowerArmourFeetItem())
        equipment.equip_item(inventory.items[len(inventory.items)-1]['item'], EquipmentSlot.FEET)
        inventory.add_item(BasicEnergyPistolItem())
        equipment.equip_item(inventory.items[len(inventory.items)-1]['item'], EquipmentSlot.RIGHT_HAND)
        inventory.add_item(BasicPlasmaCutterItem())
        equipment.equip_item(inventory.items[len(inventory.items)-1]['item'], EquipmentSlot.LEFT_HAND)