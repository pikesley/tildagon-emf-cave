from random import random

import imu
from app_components import YesNoDialog
from events.input import BUTTON_TYPES, Buttons
from system.eventbus import eventbus
from system.patterndisplay.events import PatternDisable

import app

from .lib.background import Background
from .lib.cave import Cave
from .lib.conf import conf
from .lib.explosion import Explosion
from .lib.high_score_manager import load_high_score, save_high_score
from .lib.led_manager import LEDManager
from .lib.scoreboard import Scoreboard
from .lib.ship import Ship
from .lib.title_card import TitleCard
from .pikesley.rgb_from_hue.rgb_from_hue import rgb_from_hue


class EMFCave(app.App):
    """EMFCave."""

    def __init__(self):
        """Construct."""
        eventbus.emit(PatternDisable())
        self.button_states = Buttons(self)
        self.reset()

    def reset(self):
        """Reset."""
        self.ship = Ship(0)
        self.cave = Cave()
        self.score = 0
        self.high_score = load_high_score()
        self.hue = random()
        self.inverse_hue = (self.hue + 0.5) % 1.0
        self.game_state = "ON"
        self.dialog = None
        self.background_value = 0.0
        self.highlighted_leds = conf["leds"]["highlight-indeces"]
        self.title_opacity = 1.0
        self.title_size = 40

        self.led_manager = LEDManager()
        self.title_card = TitleCard(self.hue)
        self.scoreboard = Scoreboard()

    def exit(self):
        """Quit."""
        self.reset()
        self.button_states.clear()
        self.minimise()

    def bump_hue(self):
        """Increment hue."""
        self.hue += conf["hue-increment"]
        self.inverse_hue = (self.hue + 0.5) % 1.0

    def update(self, _):
        """Update."""
        self.set_score_base(imu.acc_read())
        self.scan_buttons()

        if self.game_state == "ON":
            self.led_manager.roll_lights(self.hue)

            self.ship.descend()

            self.cave.iterate(self.hue)

            if self.cave.active_segment:
                self.score += 1
                self.high_score = max(self.score, self.high_score)

            if (self.score > 0) and (
                self.score % conf["constrictions"]["interval"] == 0
            ):
                self.cave.constrict()

            if self.ship.proximity(self.cave) <= 0:
                self.game_state = "OVER"

            self.bump_hue()

            self.title_card.iterate(self.hue)

            # self.highlighted_leds = [(i - 1) % 12 for i in self.highlighted_leds]

        elif self.game_state == "OVER":
            save_high_score(self.high_score)
            self.background_value = 0

            self.dialog = YesNoDialog(
                message="Play Again?",
                on_yes=self.reset,
                on_no=self.exit,
                app=self,
            )
            self.game_state = "PENDING"

    def draw(self, ctx):
        """Draw."""
        self.overlays = []
        self.overlays.append(
            Background(
                colour=[i * self.background_value for i in rgb_from_hue(self.hue)]
            )
        )

        if self.title_card.opacity > 0:
            self.overlays.append(self.title_card)

        self.overlays.extend(self.cave.segments)

        if self.game_state == "ON":
            self.overlays.extend(self.ship.build(self.inverse_hue))
        else:
            self.overlays.extend(Explosion(y=self.ship.y).explode())

        self.scoreboard.scores = {"score": self.score, "high-score": self.high_score}
        self.scoreboard.hue = self.inverse_hue

        self.overlays.append(self.scoreboard)
        self.draw_overlays(ctx)

        if self.dialog:
            self.dialog.draw(ctx)

    def set_score_base(self, acc):
        """Set the scoreboard number base."""
        threshold = conf["scores"]["tilt-threshold"]
        conditions = [
            acc[0] > threshold,
            acc[0] < -threshold,
            acc[1] > threshold,
            acc[1] < -threshold,
        ]
        if any(conditions):
            conf["scores"]["base-index"] = conditions.index(True)

    def scan_buttons(self):
        """Buttons."""
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

        if self.game_state == "ON":
            buttons = ["UP", "DOWN", "LEFT", "RIGHT", "CONFIRM"]
            for button in buttons:
                if self.button_states.get(BUTTON_TYPES[button]):
                    self.ship.ascend()

    def background_update(self, _):
        """Flash lights."""
        if self.game_state == "PENDING":
            self.led_manager.flame_lights()


__app_export__ = EMFCave
