from random import randint, random

from .conf import conf
from .segment import Segment


class Cave:
    """A cave."""

    def __init__(self):
        """Construct."""
        self.centre = 0
        self.segments = []
        self.active_segment = None
        self.height = conf["cave"]["height"]
        self.segment_width = conf["cave"]["segment-width"]
        self.max_segments = 240 / self.segment_width
        self.narrow_segment_probability = conf["cave"]["narrow-segments"]["probability"]

    def add_segment(self, hue):
        """Add a slice."""
        height = self.height

        if random() < self.narrow_segment_probability:
            height = self.height * conf["cave"]["narrow-segments"]["scale-factor"]

        self.segments.append(
            Segment(
                height=height, width=self.segment_width, centre=self.centre, hue=hue
            )
        )

        if len(self.segments) > self.max_segments:
            self.segments = self.segments[1:]

    def shift_centre(self, amount):
        """Shift our centre."""
        if amount < 0:
            if self.centre > (conf["screen"]["min"]["y"] + (self.height / 2)):
                self.centre += amount

        elif self.centre < (conf["screen"]["max"]["y"] - (self.height / 2)):
            self.centre += amount

    def scroll(self):
        """Move the cave to the left."""
        for segment in self.segments:
            segment.x -= self.segment_width

            if segment.x <= conf["ship"]["x-position"]:
                self.active_segment = segment

    def iterate(self, hue):
        """Move one step."""
        self.shift_centre(
            randint(-conf["cave"]["max-shift"], conf["cave"]["max-shift"])
        )
        self.add_segment(hue)
        self.scroll()

    def constrict(self):
        """Make ourself more difficult."""
        self.height -= conf["constrictions"]["increments"]["height"]
        self.segment_width += conf["constrictions"]["increments"]["speed"]
        self.narrow_segment_probability += conf["cave"]["narrow-segments"]["increment"]
