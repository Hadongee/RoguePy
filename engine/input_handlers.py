from typing import Optional
from enum import Enum

import tcod.event

from .actions import Action, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch[Action]):

    def __init__ (self):
        self.state = EventHandlerState.MAIN
        self.no_action = False

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym

        if self.state == EventHandlerState.MAIN :
            if key == tcod.event.K_UP:
                action = MovementAction(dx=0, dy=-1)
            elif key == tcod.event.K_DOWN:
                action = MovementAction(dx=0, dy=1)
            elif key == tcod.event.K_LEFT:
                action = MovementAction(dx=-1, dy=0)
            elif key == tcod.event.K_RIGHT:
                action = MovementAction(dx=1, dy=0)

            elif key == tcod.event.K_ESCAPE:
                action = EscapeAction()

        # No valid key was pressed
        return action

class EventHandlerState (Enum):
    MAIN = 0
    LOOK = 1
    