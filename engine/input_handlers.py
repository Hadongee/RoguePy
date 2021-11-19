from typing import Optional
from enum import Enum

import tcod.event
from tcod.event import KeySym

from .actions import Action, DigAction, EscapeAction, MovementAction, WaitAction, DigToggleAction, LookToggleAction, CursorMovementAction

class EventHandler(tcod.event.EventDispatch[Action]):

    def __init__ (self):
        self.state = EventHandlerState.MAIN
        self.update_game_entities = True

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
            
            elif key == KeySym.l:
                action = LookToggleAction()
                self.state = EventHandlerState.LOOK
                
            elif key == KeySym.d:
                action = DigToggleAction()
                self.state = EventHandlerState.DIG

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
                action = DigAction(dx=0, dy=-1)
            elif key == KeySym.DOWN:
                action = DigAction(dx=0, dy=1)
            elif key == KeySym.LEFT:
                action = DigAction(dx=-1, dy=0)
            elif key == KeySym.RIGHT:
                action = DigAction(dx=1, dy=0)
                
            self.state = EventHandlerState.MAIN
        
        if action != None:
            self.update_game_entities = action.update_game_entities
        
        # No valid key was pressed
        return action

class EventHandlerState (Enum):
    MAIN = 0
    LOOK = 1
    DIG = 2
    