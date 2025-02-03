from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .lib.background import Background
from .lib.conf import conf
from .lib.ship import Ship


class EMFCave(app.App):
    """EMFCave."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)

        self.ship_fall_rate = 5
        self.ship_rise_rate = 10
        self.ship = Ship(0)

    def update(self, _):
        """Update."""
        self.scan_buttons()
        self.ship.y += conf["ship"]["rates"]["fall"]

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))

        self.overlays += self.ship.build()

        self.draw_overlays(ctx)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.button_states.get(BUTTON_TYPES["UP"]):
            self.ship.y -= conf["ship"]["rates"]["rise"]


__app_export__ = EMFCave
