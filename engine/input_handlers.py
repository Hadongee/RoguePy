from typing import Optional
from enum import Enum

from components.equipment import Equipment
from items.equipment_slot import EquipmentSlot

import tcod.event
from tcod.event import KeySym

from .actions import Action, AttackAction, AttackToggleAction, DigAction, EscapeAction, InventorySelectAction, InventoryMoveAction, InventoryTabAction, MovementAction, WaitAction, DigToggleAction, LookToggleAction, CursorMovementAction, DigMovementAction, PickupAction, PickupToggleAction, PickupMovementAction, InventoryOpenAction, InventoryCloseAction

class EventHandler(tcod.event.EventDispatch[Action]):

    def __init__ (self, game):
        self.state = EventHandlerState.MAIN
        self.update_game_entities = True
        self.game = game

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if self.state == EventHandlerState.MAIN :
            if key == KeySym.UP:
                action = MovementAction(dx=0, dy=-1)
            elif key == KeySym.DOWN:
                action = MovementAction(dx=0, dy=1)
            elif key == KeySym.LEFT:
                action = MovementAction(dx=-1, dy=0)
            elif key == KeySym.RIGHT:
                action = MovementAction(dx=1, dy=0)
                
            elif key == KeySym.PERIOD:
                action = WaitAction()
            
            elif key == KeySym.q:
                left_hand_item = self.game.player.get_component(Equipment).slots[EquipmentSlot.LEFT_HAND.name]
                if left_hand_item != None:
                    action = left_hand_item.use_action
                    if left_hand_item.event_handler_state != None:
                        self.state = left_hand_item.event_handler_state
            
            elif key == KeySym.e:
                right_hand_item = self.game.player.get_component(Equipment).slots[EquipmentSlot.RIGHT_HAND.name]
                if right_hand_item != None:
                    action = right_hand_item.use_action
                    if right_hand_item.event_handler_state != None:
                        self.state = right_hand_item.event_handler_state
            
            elif key == KeySym.l:
                action = LookToggleAction()
                self.state = EventHandlerState.LOOK
                
            elif key == KeySym.p:
                action = PickupToggleAction()
                self.state = EventHandlerState.PICKUP
                
            elif key == KeySym.i:
                action = InventoryOpenAction()
                self.state = EventHandlerState.INVENTORY

            elif key == KeySym.ESCAPE:
                action = EscapeAction()
        elif self.state == EventHandlerState.LOOK :
            if key == KeySym.UP:
                action = CursorMovementAction(dx=0, dy=-1)
            elif key == KeySym.DOWN:
                action = CursorMovementAction(dx=0, dy=1)
            elif key == KeySym.LEFT:
                action = CursorMovementAction(dx=-1, dy=0)
            elif key == KeySym.RIGHT:
                action = CursorMovementAction(dx=1, dy=0)
                
            elif key == KeySym.ESCAPE:
                action = LookToggleAction()
                self.state = EventHandlerState.MAIN
        elif self.state == EventHandlerState.DIG :
            if key == KeySym.UP:
                action = DigMovementAction(dx=0, dy=-1)
            elif key == KeySym.DOWN:
                action = DigMovementAction(dx=0, dy=1)
            elif key == KeySym.LEFT:
                action = DigMovementAction(dx=-1, dy=0)
            elif key == KeySym.RIGHT:
                action = DigMovementAction(dx=1, dy=0)
                
            elif key == KeySym.ESCAPE:
                action = DigToggleAction()
                self.state = EventHandlerState.MAIN

            elif key == KeySym.RETURN:
                action = DigAction()
                self.state = EventHandlerState.MAIN
        elif self.state == EventHandlerState.PICKUP:
            if key == KeySym.UP:
                action = PickupMovementAction(dx=0, dy=-1)
            elif key == KeySym.DOWN:
                action = PickupMovementAction(dx=0, dy=1)
            elif key == KeySym.LEFT:
                action = PickupMovementAction(dx=-1, dy=0)
            elif key == KeySym.RIGHT:
                action = PickupMovementAction(dx=1, dy=0)
                
            elif key == KeySym.ESCAPE:
                action = PickupToggleAction()
                self.state = EventHandlerState.MAIN

            elif key == KeySym.RETURN:
                action = PickupAction()
                self.state = EventHandlerState.MAIN
        elif self.state == EventHandlerState.INVENTORY:
            if key == KeySym.UP:
                action = InventoryMoveAction(change=-1)
            elif key == KeySym.DOWN:
                action = InventoryMoveAction(change=1)
            elif key == KeySym.LEFT or key == KeySym.RIGHT:
                action = InventoryTabAction()
            
            elif key == KeySym.RETURN:
                action = InventorySelectAction()
            
            elif key == KeySym.ESCAPE:
                action = InventoryCloseAction()
                self.state = EventHandlerState.MAIN
        elif self.state == EventHandlerState.ATTACK:
            if key == KeySym.UP:
                action = CursorMovementAction(dx=0, dy=-1)
            elif key == KeySym.DOWN:
                action = CursorMovementAction(dx=0, dy=1)
            elif key == KeySym.LEFT:
                action = CursorMovementAction(dx=-1, dy=0)
            elif key == KeySym.RIGHT:
                action = CursorMovementAction(dx=1, dy=0)
                
            elif key == KeySym.ESCAPE:
                action = AttackToggleAction()
                self.state = EventHandlerState.MAIN

            elif key == KeySym.RETURN:
                action = AttackAction()
                self.state = EventHandlerState.MAIN
        if action != None:
            self.update_game_entities = action.update_game_entities
            self.game.update_enemies = action.update_enemies
        
        # No valid key was pressed
        return action

class EventHandlerState (Enum):
    MAIN = 0
    LOOK = 1
    DIG = 2
    PICKUP = 3
    INVENTORY = 4
    ATTACK = 5