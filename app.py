from random import randint

from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .lib.background import Background
from .lib.conf import conf
from .lib.segment import Segment
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
        self.cave = []
        self.cave_centre = 0

    def update(self, _):
        """Update."""
        self.scan_buttons()
        self.ship.y += conf["ship"]["rates"]["fall"]
        self.cave_centre = self.cave_centre + randint(-2, 2)
        self.cave.append(Segment(height=50, centre=self.cave_centre))
        for segment in self.cave:
            segment.x -= conf["cave"]["segment-width"]

        if len(self.cave) > 240 / conf["cave"]["segment-width"]:
            self.cave = self.cave[1:]

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        self.overlays.append(Background(colour=(0, 0, 0)))

        for segment in self.cave:
            self.overlays.append(segment)

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
