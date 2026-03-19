from random import randint

from tildagonos import tildagonos

from ..common.rgb_from_hue import rgb_from_hue
from .conf import conf
from .gamma import gamma_corrections

red = (255, 0, 0)
orange = (255, 127, 0)
off = (0, 0, 0)
flame_colours = [
    [gamma_corrections[int(c * conf["leds"]["brightness"]["default"])] for c in colour]
    for colour in [red, orange, off]
]


class LEDManager:
    """Manage the LEDs."""

    def __init__(self):
        """Construct."""
        self.highlight_pattern = conf["leds"]["highlight-indeces"]

    def flame_lights(self):
        """Flames."""
        for colour in flame_colours:
            tildagonos.leds[randint(1, 18)] = colour

        tildagonos.leds.write()

    def rotate_highlights(self):
        """Rotate the highlights."""
        self.highlight_pattern = [(i - 1) % 12 for i in self.highlight_pattern]

    def roll_lights(self, hue):
        """Light the lights."""
        colour = rgb_from_hue(hue)
        for i in range(12):
            brightness = conf["leds"]["brightness"]["default"]

            if i in self.highlight_pattern:
                brightness = conf["leds"]["brightness"]["highlight"]

            tildagonos.leds[12 - i] = [
                gamma_corrections[int(c * 255 * brightness)] for c in colour
            ]

        colour = rgb_from_hue(hue + 0.5)
        for i in range(6):
            brightness = conf["leds"]["brightness"]["default"]

            tildagonos.leds[i + 13C ] = [
                gamma_corrections[int(c * 255 * brightness)] for c in colour
            ]

        tildagonos.leds.write()

        self.rotate_highlights()
