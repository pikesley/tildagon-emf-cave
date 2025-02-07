from ..pikesley.rgb_from_hue.rgb_from_hue import rgb_from_hue
from ..pikesley.shapes.circle import Circle
from .conf import conf
from .proximity_sensors import proximity_to_bottom, proximity_to_top


class Ship:
    """Ship."""

    def __init__(self, y):
        """Construct."""
        self.y = y
        self.y_values = []
        self.shape = Circle

    def ascend(self):
        """Rise up."""
        if self.y >= conf["screen"]["min"]["y"]:
            self.y -= conf["ship"]["rates"]["rise"]

    def descend(self):
        """Fall down."""
        if self.y <= conf["screen"]["max"]["y"]:
            self.y += conf["ship"]["rates"]["fall"]

    def build(self, hue):
        """Draw."""
        colour = rgb_from_hue(hue)

        tail = []
        tail.append(
            self.shape(
                size=conf["ship"]["size"],
                opacity=1.0,
                centre=(conf["ship"]["x-position"], self.y),
                colour=colour,
                filled=conf["ship"]["filled"],
            )
        )

        for index, value in enumerate(reversed(self.y_values)):
            tail.append(
                self.shape(
                    size=conf["ship"]["size"]
                    * (
                        (conf["ship"]["tail"]["length"] - (index + 1))
                        / conf["ship"]["tail"]["length"]
                    ),
                    centre=(
                        conf["ship"]["x-position"]
                        - (index * conf["ship"]["tail"]["spacing"])
                        - conf["ship"]["tail"]["spacing"],
                        value,
                    ),
                    opacity=(conf["ship"]["tail"]["length"] - index)
                    / conf["ship"]["tail"]["length"],
                    colour=colour,
                    filled=conf["ship"]["filled"],
                )
            )

        self.y_values.append(self.y)
        if len(self.y_values) > conf["ship"]["tail"]["length"]:
            self.y_values = self.y_values[1:]

        return tail

    def proximity(self, cave):
        """How close are we to the wall."""
        if cave.active_segment:
            distance_from_top = proximity_to_top(
                cave.active_segment.top, self.y, conf["ship"]["size"]
            )
            distance_from_bottom = proximity_to_bottom(
                cave.active_segment.bottom, self.y, conf["ship"]["size"]
            )

            return min(distance_from_bottom, distance_from_top)

        return conf["cave"]["height"] / 2
